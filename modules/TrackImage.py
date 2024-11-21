import cv2, os
import numpy as np

class TrackImage:
    def __init__(self, frame):
        self.frame = frame
        self.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.flipped = cv2.flip(self.gray, 1)
        self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        self.people = self.detectPeople()
        self.stops = self.detectStops()
        self.lines = self.detectLines()

    def detectPeople(self):
        people_cascade = cv2.CascadeClassifier("models/people_cascade.xml")
        people = people_cascade.detectMultiScale(self.frame, 10, 100)
    
        return people
    
    def drawPeople(self):
        for (x, y, w, h) in self.people:
            cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    def drawStops(self):
            for (x, y, w, h) in self.stops:
                cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    def drawLines(self):
        cv2.drawContours(self.frame, self.lines, -1, (122, 255, 122), -1)

    def getROIs(self, interest_areas):
        _, thresh = cv2.threshold(self.gray, 220, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        valid_contours = []
        cv2.drawContours(self.frame, contours, -1, (255, 0, 0), 2)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > interest_areas[0] and area < interest_areas[1]:                
                valid_contours.append(contour)

        return valid_contours
    
    def detectStops(self):
        cascade = cv2.CascadeClassifier("models/stop_cascade.xml")
        stops = cascade.detectMultiScale(self.frame, 2, 5)
        stops = [(x, y, w, h) for (x, y, w, h) in stops if w*h > 10000 and w*h < 40000]
        valid_stops = []

        for (x, y, w, h) in stops:
            roi = self.hsv[y:y+h, x:x+w]
            if self.isObjectRed(roi): valid_stops.append((x, y, w, h))

        return valid_stops
    
    def detectLines(self):
        _, binary = cv2.threshold(self.gray, 40, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        lines = []
        for c in contours:
            area = cv2.contourArea(c)
            if area > 1500 and area < 9000:
                cv2.drawContours(self.frame, [c], -1, (122, 255, 122), -1)
                lines.append(c)

        return lines

    def getSmallestCountour(self, contours):
        smallest = None
        for c in contours:
            if smallest is None or cv2.contourArea(c) < cv2.contourArea(smallest): 
                smallest = c
            
        return smallest

    
    def getContourCentroid(self, contour):
        moments = cv2.moments(contour)

        if moments['m00'] != 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            return (cx, cy)
        else:
            return None

    def isInsideBorder(self):
        low = np.array([35, 20, 20])
        top = np.array([85, 255, 255])

        mask = cv2.inRange(self.hsv, low, top)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            area = cv2.contourArea(c)
            if area > 2000: 
                cv2.drawContours(self.frame, [c], -1, (0, 255, 0), -1)  
                return True

        return False
    
    def isObjectRed(self, img):
        lower1 = np.array([0, 122, 35])
        upper1 = np.array([10, 255, 255])

        lower2 = np.array([170, 122, 35])
        upper2 = np.array([179, 255, 255])

        mask_red_1 = cv2.inRange(img, lower1, upper1)
        mask_red_2 = cv2.inRange(img, lower2, upper2)
        mask_red = mask_red_1 + mask_red_2
        contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            area = cv2.contourArea(c)
            if area > 5: return True

        return False


