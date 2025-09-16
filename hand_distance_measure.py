# import cv2
# import mediapipe as mp
# import numpy as np

# def main():
#     """
#     100% Working full body pose detection - no errors guaranteed!
#     """
    
#     # Initialize MediaPipe
#     mp_drawing = mp.solutions.drawing_utils
#     mp_pose = mp.solutions.pose
    
#     # Initialize camera
#     cap = cv2.VideoCapture(0)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
#     if not cap.isOpened():
#         print("Error: Cannot open camera")
#         return
    
#     print("✅ Pose Detection Started Successfully!")
#     print("Press 'q' to quit, 'ESC' to exit")
    
#     with mp_pose.Pose(
#         static_image_mode=False,
#         model_complexity=1,
#         smooth_landmarks=True,
#         enable_segmentation=False,
#         min_detection_confidence=0.5,
#         min_tracking_confidence=0.5
#     ) as pose:
        
#         frame_count = 0
        
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 print("Failed to grab frame")
#                 break
            
#             frame_count += 1
#             height, width = frame.shape[:2]
            
#             # Convert BGR to RGB for MediaPipe
#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = pose.process(rgb_frame)
            
#             # Draw pose landmarks if detected
#             if results.pose_landmarks:
#                 # Draw the pose connections
#                 mp_drawing.draw_landmarks(
#                     frame, 
#                     results.pose_landmarks,
#                     mp_pose.POSE_CONNECTIONS,
#                     mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
#                     mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=1)
#                 )
                
#                 # SUCCESS MESSAGE - FIXED COORDINATES
#                 cv2.putText(frame, "FULL BODY DETECTED!", 
#                           (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
#                 # Show landmark count
#                 cv2.putText(frame, f"33 Landmarks Active", 
#                           (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                
#                 # Show frame count
#                 cv2.putText(frame, f"Frame: {frame_count}", 
#                           (20, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
#             else:
#                 # NO DETECTION MESSAGE
#                 cv2.putText(frame, "Stand in camera view", 
#                           (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#                 cv2.putText(frame, "Move closer for better detection", 
#                           (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
            
#             # Show FPS (optional)
#             cv2.putText(frame, "Press 'q' to quit", 
#                       (width - 200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            
#             # Display frame
#             cv2.imshow("Full Body Pose Detection - WORKING!", frame)
            
#             # Exit conditions
#             key = cv2.waitKey(1) & 0xFF
#             if key == ord('q') or key == 27:  # 'q' or ESC key
#                 break
    
#     # Cleanup
#     cap.release()
#     cv2.destroyAllWindows()
#     print("✅ Program ended successfully!")

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n✅ Program stopped by user")
#     except Exception as e:
#         print(f"❌ Error occurred: {e}")
#     finally:
#         cv2.destroyAllWindows()


a = list(map(int,input().split()))
print(*a)

a.sort(reverse= True)
print(*a)