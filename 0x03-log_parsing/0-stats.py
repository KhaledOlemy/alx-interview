#!/usr/bin/python3
"""TRACK STDIN"""
import sys

fileSize = 0
lineCounter = 0
allowedStatusCodes = [
    "200",
    "301",
    "400",
    "401",
    "403",
    "404",
    "405",
    "500"
]
statusCodeSummary = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

if __name__ == "__main__":
    try:
        inputLines = sys.stdin
        for line in inputLines:
            line = line.split()

            if len(line) < 6:
                continue
            lineCounter += 1

            if lineCounter <= 10:
                fileSize += int(line[-1])
                statusCode = line[-2]
                if statusCode in allowedStatusCodes:
                    statusCodeSummary[statusCode] += 1

            if lineCounter == 10:
                lineCounter = 0
                print(f"File size: {fileSize}")
                for k, v in statusCodeSummary.items():
                    if v != 0:
                        print(f"{k}: {v}")
    except KeyboardInterrupt:
        print(f"File size: {fileSize}")
        for k, v in statusCodeSummary.items():
            if v != 0:
                print(f"{k}: {v}")
