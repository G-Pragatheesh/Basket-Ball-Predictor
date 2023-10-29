import cv2

# Create a VideoCapture object to access the webcam (usually 0 or 1 for built-in webcams)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not access the webcam")
    exit()

# Define the codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi', fourcc, 20.0, (640, 480))  # Adjust the parameters as needed

# Record video for 10 seconds
duration = 10  # seconds
start_time = cv2.getTickCount()

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Write the frame to the output video
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Recording', frame)

    # Calculate elapsed time
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()

    # Break the loop if the specified duration has passed
    if elapsed_time >= duration:
        break

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and video writer
cap.release()
out.release()

# Close the OpenCV window
cv2.destroyAllWindows()

# Now, play the recorded video
cap = cv2.VideoCapture('output.avi')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Recorded Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
