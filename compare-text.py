import boto3
from datetime import datetime

def detect_text(photo, bucket, min_confidence):
    logs = list()
    now = str(datetime.now())
    tmp_log = now+" - Detecting text in "+photo
    print(tmp_log)
    logs.append(tmp_log)


    # AWS request
    client=boto3.client('rekognition')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})               
    textDetections=response['TextDetections']
    
    # Get detected words and wrap it in one phrase (list of the words)
    phrase = list()
    for text in textDetections:
        if(text['Type'] == 'WORD'):
            word = text['DetectedText']
            confidence = float(text['Confidence'])

            # Check if the confidence is enough
            if(confidence >= min_confidence):
                # Add the word to the phrase
                phrase.append(word)
                now = str(datetime.now())
                tmp_log = now+" - '"+word+"' detected with "+"{:.3f}".format(confidence)+"% of confidence - Acceptable"
                print(tmp_log)
                logs.append(tmp_log)
            else:
                # Discard the word as we dont have enough confidence
                now = str(datetime.now())
                tmp_log = now+" - '"+word+"' detected with "+"{:.3f}".format(confidence)+"% of confidence - Unacceptable"
                print(tmp_log)
                logs.append(tmp_log)
    return phrase,logs

def compare_phrases(phrase_control,phrase_test,strict=True):
    result = phrase_control == phrase_test
    now = str(datetime.now())
    tmp_log = now + " - Comparing phrases - "+ str(result)
    print(tmp_log)
    return result,[tmp_log]

def compare_result(result,expected):
    test_passed = result == expected
    if test_passed:
        now = str(datetime.now())
        tmp_log = now + " - got "+str(result)+", expected "+str(expected)+" - Test Passed"
        print(tmp_log)
    else:
        now = str(datetime.now())
        tmp_log = now + " - got "+str(result)+", expected "+str(expected)+" - Test Failed"
        print(tmp_log)
    return [tmp_log]

def main():

    # Initial params
    logs = []
    bucket='tareaps'
    photo_control='meme-A.jpg'
    photo_test='meme-B.jpg'
    min_confidence=90
    expected=True
    
    # Initial Logging
    now = str(datetime.now())
    tmp_log = now+" - Bucket: "+bucket
    print(tmp_log)
    logs.append(tmp_log)

    now = str(datetime.now())
    tmp_log = now+" - Photo control: "+photo_control
    print(tmp_log)
    logs.append(tmp_log)

    now = str(datetime.now())
    tmp_log = now+" - Photo test: "+photo_test
    print(tmp_log)
    logs.append(tmp_log)

    now = str(datetime.now())
    tmp_log = now+" - Minimal confidence: "+str(min_confidence)
    print(tmp_log)
    logs.append(tmp_log)
    
    # Get phrase from control image
    phrase_control,tmp_log=detect_text(photo_control,bucket,min_confidence)
    logs+=tmp_log
    
    # Get phrase from testing image
    phrase_test,tmp_log=detect_text(photo_test,bucket,min_confidence)
    logs+=tmp_log

    # Compare the text in both images
    result,tmp_log=compare_phrases(phrase_control,phrase_test)
    logs+=tmp_log

    tmp_log=compare_result(result,expected)

if __name__ == "__main__":
    main()