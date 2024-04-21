import cv2
import webbrowser


#Chose if you want scan a new qrcode
response = input("\nDo you want to scan a new qrcode? (y/n): ")
response_lower = response.lower() #Conver in lower case

codeqr = ()
if response_lower == 'y':
#Initalize the cam
    cap = cv2.VideoCapture(0)

    #Initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()
        # _ variabile che indica se la lettura del frame è avvenuta correttamente
        #in Python _ viene usato per indicare una variabile destinata ad essere ignorata o non usata

        # detect and decode
        data, one, _ = detector.detectAndDecode(img)
        #occorre indicare one e _ perchè detector.detectAndDecode(img) restituisce 3 valori
        #ma serve solo data gli altri poi li ignora

        # check if there is a QRCode in the image
        if data:
            codeqr = data
            break
        # display the result
        cv2.imshow("QRCODEscanner app", img)    
        if cv2.waitKey(1) == ord("q"):
            break
else:
    pass

link = webbrowser.open(str(codeqr)) #apre il link nel qrcode
cap.release() #smette di usare la fotocamera
cv2.destroyAllWindows()