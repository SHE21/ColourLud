import cv2


def getCapture(firFile, QLabel):
    camera_port = 0

    nFrames = 30

    camera = cv2.VideoCapture(camera_port)
    # camera.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
    # camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 160)

    #file = "images/imagenTeste.png"

    print("Digite <ESC> para sair / <s> para Salvar")

    emLoop = True

    while (emLoop):

        retval, img = camera.read()
        cv2.imshow('Foto', img)


        k = cv2.waitKey(100)

        if k == 27:
            emLoop = False

        elif k == ord('s'):
            cv2.imwrite(firFile, img)
            emLoop = False

    cv2.destroyAllWindows()
    camera.release()
    return firFile


getCapture("images/imagenTeste.png", None)
