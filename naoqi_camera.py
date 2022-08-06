#coding=utf-8
from os import listdir
from os.path import isfile, join
import time

import qi
import argparse
import sys
import time
import vision_definitions

from math import *
import matplotlib.pyplot as plt
import numpy

import cv2
from naoqi import ALProxy

def main(session):
    # Get the service ALVideoDevice.
    video_service = session.service("ALVideoDevice")

    # Register a Generic Video Module
    resolution = vision_definitions.kQVGA # 160*120
    colorSpace = vision_definitions.kBGRColorSpace
    fps = 10

    nameId = video_service.subscribeCamera("video" + str(time.time()), 0, resolution, colorSpace, fps)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    outV = cv2.VideoWriter("/Users/Melanie/Documents/Waterloo/Intergenerational/tangram/video_" + str(time.time()) + ".avi", fourcc, 10.0, (320, 240))

    #ser.write('z')
    while 1:
        ct = time.time()
        nao_image = video_service.getImageRemote(nameId)

        img = (numpy.reshape(numpy.frombuffer(nao_image[6], dtype = '%iuint8' %nao_image[2]), (nao_image[1], nao_image[0], nao_image[2])))
        outV.write(img)
        
        cv2.imshow("window", img)
        if cv2.waitKey(1) == 27:
            break
        
    outV.release()
    video_service.unsubscribe(nameId)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.100", help="Robot IP address. On robot or Local Naoqi: use '10.42.0.31'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
            "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
