{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6f4de25e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import face_recognition\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81087eaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "video_capture = cv2.VideoCapture(0)\n",
    "# Load a sample picture and learn how to recognize it.\n",
    "image = face_recognition.load_image_file(\"C:\\\\Users\\\\madhu\\\\OneDrive\\\\Desktop\\\\fc photo.jpeg\")\n",
    "face_encoding = face_recognition.face_encodings(image)[0]\n",
    "known_face_encodings = [  face_encoding,]\n",
    "known_face_names = [ \"MADHU 21695A3502\"]\n",
    "# Initialize some variables\n",
    "face_locations = []\n",
    "face_encodings = []\n",
    "face_names = []\n",
    "process_this_frame = True\n",
    "while True:\n",
    "    # Grab a single frame of video\n",
    "    ret, frame = video_capture.read()\n",
    "    # Resize frame of video to 1/4 size for faster face recognition processing\n",
    "    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)\n",
    "    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)\n",
    "    rgb_small_frame = small_frame[:, :, ::-1]\n",
    "    # Only process every other frame of video to save time\n",
    "    if process_this_frame:\n",
    "        # Find all the faces and face encodings in the current frame of video\n",
    "        face_locations = face_recognition.face_locations(rgb_small_frame)\n",
    "        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)\n",
    "        face_names = []\n",
    "        for face_encoding in face_encodings:\n",
    "            # See if the face is a match for the known face(s)\n",
    "            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)\n",
    "            name = \"Unknown\"\n",
    "            # # If a match was found in known_face_encodings, just use the first one.\n",
    "            # if True in matches:\n",
    "            #     first_match_index = matches.index(True)\n",
    "            #     name = known_face_names[first_match_index]\n",
    "            # Or instead, use the known face with the smallest distance to the new face\n",
    "            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)\n",
    "            best_match_index = np.argmin(face_distances)\n",
    "            if matches[best_match_index]:\n",
    "                name = known_face_names[best_match_index]\n",
    "            face_names.append(name)\n",
    "    process_this_frame = not process_this_frame\n",
    "    # Display the results\n",
    "    for (top, right, bottom, left), name in zip(face_locations, face_names):\n",
    "        # Scale back up face locations since the frame we detected in was scaled to 1/4 size\n",
    "        top *= 4\n",
    "        right *= 4\n",
    "        bottom *= 4\n",
    "        left *= 4\n",
    "        # Draw a box around the face\n",
    "        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)\n",
    "        # Draw a label with a name below the face\n",
    "        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)\n",
    "        font = cv2.FONT_HERSHEY_DUPLEX\n",
    "        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)\n",
    "    # Display the resulting image\n",
    "    cv2.imshow('Video', frame)\n",
    "    # Hit 'q' on the keyboard to quit!\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "# Release handle to the webcam\n",
    "video_capture.release()\n",
    "\n",
    "        \n",
    "            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21ef99a3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7ff2e48",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cdbc10d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0dc29df1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "254d61a7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0f4a02e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
