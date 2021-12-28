from ..models import *
# from . import LoggerDataV1_0
# from . import ApiPostCallV1_0, ErrorCodes
from . import ErrorCodes
import logging
logger = logging.getLogger(__name__)
from django.conf import settings
import sys,inspect


def upsertLanguage(self,request,format=None):
    # It contains the name of the file and the function
    # FunctionName = FileName + "." + sys._getframe().f_code.co_name
    # LoggerDataV1_0.LogDataV1_0(settings.SERVER_TYPE, request['ipAddress'], request['PubIp'], FunctionName,
    #                            "Function called",request)
    
        # sendData={}
        # request['UserTypes'] = ['SGGOD','SGCD']
        # if ApiPostCallV1_0.checkAuthorisation(self,request) is False:
        #     log_id = LoggerDataV1_0.LogDataV1_0(settings.SERVER_TYPE, request['ipAddress'], request['PubIp'],
        #                                FunctionName, "User not authorized",
        #                                request)
        #     sendData = {}
        #     sendData['R_ID'] = log_id
        #     sendData['RC'] = ErrorCodes.ERROR_CODE_LIST["USER_NOT_AUTHORIZED"]
        #     sendData['RS'] = "USER_NOT_AUTHORIZED"
        #     sendData['RV'] = None
        #     return sendData
        # if "languageId" in request:  # if the language id is in request then update operation will be performed
        #     language= Language.objects.get(LanguageId=request['languageId'])
        #     language.LanguageName = request['languageName']
        #     language.LanguageNameInEnglish = request['languageNameInEnglish']
        #     language.save()
        # new centre is added
        language,created = Language.objects.get_or_create(LanguageName=request['languageName'])
        language.LanguageNameInEnglish = request['languageNameInEnglish']
        language.save()
        log_id = LoggerDataV1_0.LogDataV1_0(settings.SERVER_TYPE, request['ipAddress'], request['PubIp'], FunctionName, "Succesful post",
                                   request)
        sendData['R_ID'] = log_id
        sendData['RC'] = ErrorCodes.ERROR_CODE_LIST["SUCCESS"]
        sendData['RS'] = "SUCCESS"
        sendData['RV'] = {"languageId":language.LanguageId}
        return sendData
    except Exception as e:
        LoggerDataV1_0.Debug()
        log_id = LoggerDataV1_0.LogDataV1_0(settings.SERVER_TYPE, request['ipAddress'], request['PubIp'], FunctionName, e, request)
        sendData = {}
        sendData['R_ID'] = log_id
        sendData['RC'] = ErrorCodes.ERROR_CODE_LIST["RECORD_NOT_INSERTED"]
        sendData['RS'] = "RECORD_NOT_INSERTED"
        sendData['RV'] = None
        return sendData
