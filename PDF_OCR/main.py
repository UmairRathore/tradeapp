
import cv2
import os
import numpy as np
import ctypes  # An included library with Python install.
import shutil
import csv
import sys

from pdf2image import convert_from_path

configPath_for_checkboxpart = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/CheckboxPart.cfg"
weightsPath_for_checkboxpart = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/CheckboxPart.weights"
configPath_for_row = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/CheckboxPart_row.cfg"
weightsPath_for_row = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/CheckboxPart_row.weights"
configPath_for_mark = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/mark.cfg"
weightsPath_for_mark = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/mark.weights"
configPath_for_countrypart = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/CountryPart.cfg"
weightsPath_for_countrypart = os.path.dirname(os.path.realpath(sys.argv[0]))+"/model/CountryPart.weights"

# C:\wamp64\www\tradeapp\PDF_OCR\qds-LEVANT-05-03-22-BIDAUD.pdf
SOURCE_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+"/test/pdfs/"
IMAGE_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+"/test/test images from pdfs/"
RESULT_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/test/result/'
Exception_IMAGES = os.path.dirname(os.path.realpath(sys.argv[0]))+'/test/test exception images/'
PROCESSED_PDFS = os.path.dirname(os.path.realpath(sys.argv[0]))+"/test/processed pdfs/"
Exception_PDFS = os.path.dirname(os.path.realpath(sys.argv[0]))+"/test/test exception pdfs/"


# SOURCE_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+"/PDFs/"
# IMAGE_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+"/Images from PDF/"
# RESULT_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/Result/'
# Exception_IMAGES = os.path.dirname(os.path.realpath(sys.argv[0]))+'/Exception Images/'
# PROCESSED_PDFS = os.path.dirname(os.path.realpath(sys.argv[0]))+"/Processed PDFs/"
# Exception_PDFS = os.path.dirname(os.path.realpath(sys.argv[0]))+"/Exception PDFs"

# COLUMN_NAMES = ["Agrément et confort du bateau", "Les espaces de vie sont ils suffisants", "Propreté et entretien",
#                 "Amabilité", "Efficacité", "Disponibilité",
#                 "Amabilité", "Efficacité", "Disponibilité",
#                 "Respect du descriptif", "Information sur le déroulement des journées",
#                 "Qualité", "Variété", "Quantité",
#                 "L'impression globale sur votre séjour", "Recommanderez vois cette croisère ?"]
# COUNTRYPART_COLUMN_NAMES = ["COTE AZUR", "SARDAIGNE", "CORSE",
#                             "TURQUOISES", "GRENADINES", "ANTIGUA & BARBUDA",
#                             "CUBA", "BAHAMAS", "ILES GRECQUES",
#                             "ILE MAURICE", "SEYCHELLES", "MALDIVES",
#                             "THAILANDE", "POLYNESIE", "CROATIE"
#                             ]


COLUMN_NAMES = [
"Quelle est La probabilité que vous recommandiez Catlante à un de vos proches ?"
# "Qualité des informations reçues avant votre séjour",
# "Amabilité et suivi de l'agent de la réservation au séjour",
# "Agrément et confort du bateau",
# "Aménagement et confort de la cabine",
# "Qualité des espaces communs intérieurs et extérieurs",
# "Propreté et entretien",
# "Amabilité",
# "Efficacité",
# "Disponibilité",
# "Amabilité",
# "Efficacité",
# "Disponibilité",
# "Conformité au descriptif",
# "Qualité de l'itinéraire et des escales",
# "Informations reçues à bord sur les escales",
# "Sentiment de respect de l'environement et de connexion avec la nature",
# "Qualité",
# "Variété",
# "Quantité",
# "Impression globale sur votre séjour",
# "Aviez-vous deja effectue des croisiere (voile, yacht ou autres types...)",
# "Auriez-vous aimé recevoir d'autre informations lors de votre reservation",
# "Souhaitez-vous être informé(e) par mail de nos prochaines croisères"
]



COUNTRYPART_COLUMN_NAMES = [
# "Grenadines"
# "St Barth", "Guadeloupe & Dominique",
# "Antigua & Barbuda", "Seychelles", "Madagascar",
# "Corse", "Sardaigne", "Elbe-Toscane",
# "Provence", "Sicile - Eolienes", "Baléares",
# "Iles Canaries", "Croatie", "Iles grecques"
]

checkboxpart_net = cv2.dnn_Net
row_net = cv2.dnn_Net
mark_net = cv2.dnn_Net
countrypart_net = cv2.dnn_Net

confThreshold = 0.8  # Confidence threshold
nmsThreshold = 0.6 # Non-maximum suppression threshold
number_of_rows = [3, 3, 3, 2, 3, 2]
import time
def Load_model():
    global checkboxpart_net
    checkboxpart_net = cv2.dnn.readNetFromDarknet(configPath_for_checkboxpart, weightsPath_for_checkboxpart)

    global row_net
    row_net = cv2.dnn.readNetFromDarknet(configPath_for_row, weightsPath_for_row)

    global mark_net
    mark_net = cv2.dnn.readNetFromDarknet(configPath_for_mark, weightsPath_for_mark)

    global countrypart_net
    countrypart_net = cv2.dnn.readNetFromDarknet(configPath_for_countrypart, weightsPath_for_countrypart)

def list_pdf_files(path):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.pdf')]
    onlyfiles.sort()
    return onlyfiles
def list_images(path):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.jpg')]
    onlyfiles.sort()
    return onlyfiles

def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # print("The Array is: ", layersNames)
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i - 1] for i in net.getUnconnectedOutLayers()]
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
def DetectionProcess(image, outs):
    classIds = []
    confidences = []
    boxes = []
    st = time.time();
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * image.shape[1])
                center_y = int(detection[1] * image.shape[0])
                width = int(detection[2] * image.shape[1])
                height = int(detection[3] * image.shape[0])
                left = int(center_x - width / 2)
                if (left < 0): left = 0
                top = int(center_y - height / 2)
                if (top < 0): top = 0
                right = left + int(width)
                if (right > image.shape[1]): right = image.shape[1] - 1
                bottom = top + int(height * 1.0)
                if (bottom > image.shape[0]): bottom = image.shape[0] - 1

                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, right, bottom])

    # return boxes, classIds

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    results = []
    newClassIDs = []
    for i in indices:
        results.append(boxes[i])
        newClassIDs.append(classIds[i])
    return results, newClassIDs
    # if len(indices) < 1: return [0, 0, 0, 0], -1

    # max_conf = 0.0
    # max_index = 0
    # for i in indices:
    #     index = i[0]
    #     if confidences[index] > max_conf:
    #         max_conf = confidences[index]
    #         max_index = index
    #
    # return boxes[max_index], classIds[max_index]

def OrderFunc(e):
    return e[1]


if __name__ == '__main__':
    Load_model()
    ls_pdfs = list_pdf_files(SOURCE_FOLDER)
    for input_pdf in ls_pdfs:

        pdfFileName = os.path.join(SOURCE_FOLDER, input_pdf)
        movePDFFilename = os.path.join(PROCESSED_PDFS, input_pdf)
        try:
            images = convert_from_path(pdfFileName)
            pathname, extension = os.path.splitext(input_pdf)
            filename = pathname.split('/')
            strPara = filename[-1];
            flag = False
            # strPara = os.path.basename(input_pdf).split('.')[0]
            for i in range(len(images)):
                # Save pages as images in the pdf
                imageFileName  =strPara + ".jpg"
                if len(images) > 1:

                    imageFileName = strPara + '_page' + str(i) + '.jpg'
                moveImageFilename = os.path.join(Exception_IMAGES, imageFileName)
                imageFileName = os.path.join(IMAGE_FOLDER, imageFileName)

                images[i].save(imageFileName, 'JPEG')
                startTime = time.time()

                # baseName = os.path.basename(imageFileName).split('.')[0]
                # baseName += ".csv"

                pathname, extension = os.path.splitext(imageFileName)
                filename = pathname.split('/')
                baseName = filename[-1]
                baseName += ".csv"

                outputCSVFilename = os.path.join(RESULT_FOLDER, baseName)

                # try:
                # img = cv2.imread(imageFileName)
                img = cv2.imdecode(np.fromfile(imageFileName, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
                print(imageFileName)
                h, w, c = img.shape
                maxValue = h
                if h > w:
                    maxValue = w
                ratio = maxValue / 800
                newsize = (int(w / ratio), int(h / ratio))
                imgresized = cv2.resize(img, newsize, cv2.INTER_LINEAR)
                # cv2.imshow("original", img)
                # cv2.waitKey(0)
                blob = cv2.dnn.blobFromImage(imgresized, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)
                # Sets the input to the network
                checkboxpart_net.setInput(blob, "data")
                # Runs the forward pass to get output of the output layers
                outs = checkboxpart_net.forward(getOutputsNames(checkboxpart_net))
                detection, classid = DetectionProcess(imgresized, outs)
                result = []
                country_part = []
                for i in range(16):
                    result.append("")
                for i in range(15):
                    country_part.append("")
                if len(detection) == 0 and len(images) == 1:
                    flag = True
                    continue
                if len(detection) != 1:
                    shutil.move(imageFileName, moveImageFilename)
                    continue
                for rect in detection:
                    imgresized = cv2.rectangle(imgresized, (rect[0], rect[1]), (rect[2], rect[3]), (0, 0, 255), 4)
                    y1 = int((rect[1] - 5) * ratio)
                    y2 = int((rect[3] + 10) * ratio)
                    x1 = int((rect[0] - 5) * ratio)
                    x2 = int((rect[2] + 10) * ratio)
                    crop_img = img[y1:y2, x1:x2]
                    h, w, c = crop_img.shape
                    if w > h:
                        crop_img = cv2.rotate(crop_img, cv2.ROTATE_90_CLOCKWISE)
                        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                    blob1 = cv2.dnn.blobFromImage(crop_img, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)
                    # Sets the input to the network
                    row_net.setInput(blob1, "data")
                    # Runs the forward pass to get output of the output layers
                    outs1 = row_net.forward(getOutputsNames(row_net))
                    detection1, classid1 = DetectionProcess(crop_img, outs1)
                    if len(detection1) == 0:
                        continue
                    for i in range(len(detection1) - 1):
                        for j in range(i + 1, len(detection1)):
                            if detection1[i][1] > detection1[j][1]:
                                temp = detection1[i]
                                detection1[i] = detection1[j]
                                detection1[j] = temp
                                temp = classid1[i]
                                classid1[i] = classid1[j]
                                classid1[j] = temp

                    # detection1.sort(key=OrderFunc)
                    if len(detection1) != 6:
                        shutil.move(imageFileName, moveImageFilename)

                    if classid1[0] == 1:
                        detection1.reverse()
                        img = cv2.rotate(img, cv2.ROTATE_180)

                    if len(detection1) == 6:
                        index = 0
                        for i in range(6):
                            rect1 = detection1[i]
                            # for rect1 in detection1:
                            # imgresized1 = cv2.rectangle(crop_img, (rect1[0], rect1[1]), (rect1[2], rect1[3]),
                            #                             (0, 0, 255), 4)
                            h, w, c = crop_img.shape
                            y1 = int((rect1[1] - 10))
                            y2 = int((rect1[3] + 20))
                            x1 = int((rect1[0] - 10))
                            x2 = int((rect1[2] + 20))
                            if y1 < 0:
                                y1 = 0
                            if x1 < 0:
                                x1 = 0
                            if y2 > h:
                                y2 = h
                            if x1 > w:
                                x1 = w
                            row_img = crop_img[y1:y2, x1:x2]

                            if classid1[0] == 1:
                                row_img = cv2.rotate(row_img, cv2.ROTATE_180)
                            blob2 = cv2.dnn.blobFromImage(row_img, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)
                            # Sets the input to the network
                            mark_net.setInput(blob2, "data")
                            # Runs the forward pass to get output of the output layers
                            outs1 = mark_net.forward(getOutputsNames(mark_net))
                            detection2, classid2 = DetectionProcess(row_img, outs1)
                            detection2.sort(key=OrderFunc)
                            h, w, c = row_img.shape
                            # cv2.imshow("row", row_img)
                            # cv2.waitKey(0)
                            avgH = h / number_of_rows[i]
                            avgW = w / 5
                            # for j in range(number_of_rows[i]):

                            for rect2 in detection2:
                                imgresized1 = cv2.rectangle(row_img, (rect2[0], rect2[1]), (rect2[2], rect2[3]), (0, 0, 255), 4)

                                # cv2.imshow(imageFileName, imgresized1)
                                # cv2.waitKey(0)
                                # cv2.destroyAllWindows()
                                cntY = (rect2[1] + rect2[3]) / 2
                                cntX = (rect2[0] + rect2[2]) / 2
                                indexY = int(cntY / avgH)
                                indexX = int(cntX / avgW)
                                index1 = index + indexY
                                if result[index1] != "":
                                    qtr = ", " + str(indexX + 1)
                                    result[index1] += qtr
                                    continue
                                result[index1] = str(indexX + 1)

                            index += number_of_rows[i]
                            # for rect2 in detection2:
                            #
                            #     imgresized1 = cv2.rectangle(row_img, (rect2[0], rect2[1]), (rect2[2], rect2[3]), (0, 0, 255), 4)

                            # cv2.imshow(input_image, imgresized1)
                            # cv2.waitKey(0)

                        # cv2.imwrite(outputFilename, crop_img)
                        # cv2.imshow("tt", crop_img)
                        # cv2.waitKey(0)
                h, w, c = img.shape
                maxValue = h
                if h > w:
                    maxValue = w
                ratio = maxValue / 800
                newsize = (int(w / ratio), int(h / ratio))
                imgresized_img = cv2.resize(img, newsize, cv2.INTER_LINEAR)
                # cv2.imshow("11", imgresized_img)
                # cv2.waitKey(0)
                blob1 = cv2.dnn.blobFromImage(imgresized_img, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)
                # Sets the input to the network
                countrypart_net.setInput(blob1, "data")
                # Runs the forward pass to get output of the output layers
                outs = countrypart_net.forward(getOutputsNames(countrypart_net))
                detection, classid = DetectionProcess(imgresized_img, outs)
                for rect in detection:
                    imgresized = cv2.rectangle(imgresized_img, (rect[0], rect[1]), (rect[2], rect[3]), (0, 0, 255), 4)
                    # y1 = int((rect[1] - 5) * ratio)
                    # y2 = int((rect[3] + 10) * ratio)
                    # x1 = int((rect[0] - 5) * ratio)
                    # x2 = int((rect[2] + 10) * ratio)
                    y1 = int((rect[1] + 5) * ratio)
                    y2 = int((rect[3] - 5) * ratio)
                    x1 = int((rect[0] + 5) * ratio)
                    x2 = int((rect[2] - 5) * ratio)

                    crop_img = img[y1:y2, x1:x2]
                    # cv2.imwrite(outimageFileName, crop_img)
                    blob2 = cv2.dnn.blobFromImage(crop_img, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)
                    # Sets the input to the network
                    mark_net.setInput(blob2, "data")
                    # Runs the forward pass to get output of the output layers
                    outs = mark_net.forward(getOutputsNames(mark_net))
                    detection2, classid1 = DetectionProcess(crop_img, outs)
                    h, w, c = crop_img.shape
                    # cv2.imshow("row", row_img)
                    # cv2.waitKey(0)
                    avgH = h / 5
                    avgW = w / 3
                    imgresized1 = []
                    for rect2 in detection2:
                        imgresized1 = cv2.rectangle(crop_img, (rect2[0], rect2[1]), (rect2[2], rect2[3]), (0, 0, 255), 4)
                        font = cv2.FONT_HERSHEY_SIMPLEX

                        # cv2.imshow(imageFileName, imgresized1)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                        cntY = (rect2[1] + rect2[3]) / 2
                        cntX = (rect2[0] + rect2[2]) / 2
                        indexY = int(cntY / avgH)
                        indexX = int(cntX / avgW)
                        index1 = 3 * indexY + indexX + 1
                        # if country_part[index1 - 1] != "":
                        #     qtr = ", " + str(indexX + 1)
                        #     country_part[index1 - 1] += qtr
                        #     continue
                        cv2.putText(imgresized1, str(index1), (int(cntX), int(cntY)), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
                        country_part[index1 - 1] = "1"
                        # country_part[index1 - 1] = str(index1)
                        print(index1)
                output = []
                for i in range(16):
                    row = []
                    row.append(COLUMN_NAMES[i])
                    row.append(result[i])
                    output.append(row)
                for i in range(15):
                    row = []
                    row.append(COUNTRYPART_COLUMN_NAMES[i])
                    row.append(country_part[i])
                    output.append(row)
                print(output)
                # opening the csv file in 'a+' mode
                file = open(outputCSVFilename, 'w+', newline='')

                # writing the data into the file
                with file:
                    write = csv.writer(file)
                    write.writerows(output)

                endTime = time.time()
                print(f" {imageFileName}  processing time    is {endTime - startTime}")
                print("\n")
            if flag == True:
                exceptionFilename = os.path.join(Exception_PDFS, input_pdf)
                shutil.move(pdfFileName, exceptionFilename)
                continue
            shutil.move(pdfFileName, movePDFFilename)
        except Exception as e:
            print(f"Une erreur inattendue est survenue : {e}")
            exceptionFilename = os.path.join(Exception_PDFS, input_pdf)
            shutil.move(pdfFileName, exceptionFilename)
