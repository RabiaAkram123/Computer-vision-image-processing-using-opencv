# # ############# video.py############
# # # This script captures video from the default camera and displays it in a window.

# import cv2
# cap = cv2.VideoCapture(0) 
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # cv2.imshow("Video Feed", gray)
#     cv2.imshow("Video Feed", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


# # ##################from  pc###################
# import cv2
# cap = cv2.VideoCapture(0)
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('output.avi',fourcc,.0,(640,480))
# print(cap.isOpened())
# while (cap.isOpened()):

#     ret, frame = cap.read()
#     if ret==True:
#       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#       out.write(frame)
#       if not ret:
#         break
#       cv2.imshow("Video Feed", frame)
#       if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     else:
#      break
# cap.release()
# out.release()
# cv2.destroyAllWindows()

