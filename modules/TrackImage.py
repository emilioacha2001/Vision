import cv2, os
import numpy as np

class TrackImage:
    def __init__(self, frame):
        self.frame = frame
        self.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.flipped = cv2.flip(self.gray, 1)
        self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        self.people = self.detectPeople()
        self.redLights = self.detectRedLights()
        self.lines = self.detectLines()

    def detectPeople(self):
        rois = self.getROIs([15000, 1000000])
        face_cascade = cv2.CascadeClassifier("models/haarcascade_fullbody.xml")

        faces = []
        for roi in rois:
            x, y, w, h = cv2.boundingRect(roi)
            roi_faces = face_cascade.detectMultiScale(self.gray[y:y+h, x:x+w], 1.01, 2)
            if len(roi_faces) == 0:
                roi_faces = face_cascade.detectMultiScale(self.flipped[y:y+h, x:x+w], 1.01, 2)
            if len(roi_faces) > 0:
                roi_faces[:, 0] += x
                roi_faces[:, 1] += y
                faces.append(roi_faces[0])
    
        return faces
    
    def drawPeople(self):
        for (x, y, w, h) in self.people:
            cv2.rectangle(self.frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    def drawRedLights(self):
        for contour in self.redLights:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    def drawLines(self):
        for line in self.lines:
            cv2.rectangle(self.frame, (line[0], line[1]), (line[0]+line[2], line[1]+line[3]), (0, 255, 100), 2)

    def getROIs(self, interest_areas):
        _, thresh = cv2.threshold(self.gray, 220, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        valid_contours = []
        cv2.drawContours(self.frame, contours, -1, (255, 0, 0), 2)
        for contour in contours:
            area = cv2.contourArea(contour)
            print(area)
            if area > interest_areas[0] and area < interest_areas[1]:                
                valid_contours.append(contour)

        return valid_contours
    
    def detectRedLights(self):
        lower1 = np.array([0, 205, 30])
        upper1 = np.array([10, 255, 255])

        lower2 = np.array([170, 205, 30])
        upper2 = np.array([179, 255, 255])

        mask_red_1 = cv2.inRange(self.hsv, lower1, upper1)
        mask_red_2 = cv2.inRange(self.hsv, lower2, upper2)
        mask = mask_red_1 + mask_red_2
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        valid_stops = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:
                valid_stops.append(contour)

        return valid_stops
    
    def detectLines(self):
        rois = self.getROIs([1000, 5000])
        lines = []
        for roi in rois:
            lines.append(cv2.boundingRect(roi))

        return lines
