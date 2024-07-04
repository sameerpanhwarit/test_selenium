class Filter:
    def __init__(self, unfilter_list):
        self.unfilter_list = unfilter_list
        self.parentList = []
        self.childList = []

    def filter_list(self):
        for element in self.unfilter_list:
            if "_" in element:
                if element not in self.childList:
                    self.childList.append(element)
            else:
                if element not in self.parentList:
                    self.parentList.append(element)

    def create_dict(self):
        filterDict = {}
        for parent in self.parentList:
            temp_list = []
            for child in self.childList:
                if parent in child:
                    temp_list.append(child)
                    print(temp_list)
            filterDict[parent] = temp_list
        return filterDict
    
    def show_dict(self,filterDict):
        for key, values in filterDict.items():
            print(f'{key} - {values} \n')


Unfilter_list = ['compInfo', 'compInfo_PAK', 'directDeposit', 'emailInfo', 'emailInfo_candidate', 'emailInfo_dependent', 'emailInfo_employee', 'emergencyContactPrimary', 'employmentInfo', 'globalAssignmentInfo', 'globalInfo', 'globalInfo_ARE', 'globalInfo_ARG', 'globalInfo_AUS', 'globalInfo_AUT', 'globalInfo_BEL', 'globalInfo_BGD', 'globalInfo_BRA', 'globalInfo_CAN', 'globalInfo_CHE', 'globalInfo_CHL', 'globalInfo_CHN', 'globalInfo_COL', 'globalInfo_CZE', 'globalInfo_DEU', 'globalInfo_DNK', 'globalInfo_EGY', 'globalInfo_ESP', 'globalInfo_FIN', 'globalInfo_FRA', 'globalInfo_GBR', 'globalInfo_GTM', 'globalInfo_HKG', 'globalInfo_HUN', 'globalInfo_IDN', 'globalInfo_IND', 'globalInfo_IRL', 'globalInfo_ITA', 'globalInfo_JPN', 'globalInfo_KOR', 'globalInfo_LKA', 'globalInfo_MEX', 'globalInfo_MYS', 'globalInfo_NLD', 'globalInfo_NOR', 'globalInfo_NZL', 'globalInfo_OMN', 'globalInfo_PER', 'globalInfo_PHL', 'globalInfo_POL', 'globalInfo_PRT', 'globalInfo_QAT', 'globalInfo_ROU', 'globalInfo_RUS', 'globalInfo_SAU', 'globalInfo_SGP', 'globalInfo_SWE', 'globalInfo_THA', 'globalInfo_TUR', 'globalInfo_TWN', 'globalInfo_USA', 'globalInfo_VEN', 'globalInfo_VNM', 'globalInfo_ZAF', 'homeAddress', 'homeAddress_ARE', 'homeAddress_ARG', 'homeAddress_AUS', 'homeAddress_AUT', 'homeAddress_BEL', 'homeAddress_BGD', 'homeAddress_BRA', 'homeAddress_CAN', 'homeAddress_CHE', 'homeAddress_CHL', 'homeAddress_CHN', 'homeAddress_COL', 'homeAddress_CZE', 'homeAddress_DEU', 'homeAddress_DNK', 'homeAddress_EGY', 'homeAddress_ESP', 'homeAddress_FIN', 'homeAddress_FRA', 'homeAddress_GBR', 'homeAddress_GTM', 'homeAddress_HKG', 'homeAddress_HUN', 'homeAddress_IDN', 'homeAddress_IND', 'homeAddress_ITA', 'homeAddress_JPN', 'homeAddress_KOR', 'homeAddress_LKA', 'homeAddress_MEX', 'homeAddress_MYS', 'homeAddress_NLD', 'homeAddress_NOR', 'homeAddress_NZL', 'homeAddress_OMN', 'homeAddress_PER', 'homeAddress_PHL', 'homeAddress_POL', 'homeAddress_PRT', 'homeAddress_QAT', 'homeAddress_ROU', 'homeAddress_RUS', 'homeAddress_SAU', 'homeAddress_SGP', 'homeAddress_SWE', 'homeAddress_THA', 'homeAddress_TUR', 'homeAddress_TWN', 'homeAddress_USA', 'homeAddress_VEN', 'homeAddress_VNM', 'homeAddress_ZAF', 'imInfo', 'jobInfo', 'jobInfo_ARE', 'jobInfo_ARG', 'jobInfo_AUS', 'jobInfo_AUT', 'jobInfo_BEL', 'jobInfo_BGD', 'jobInfo_BRA', 'jobInfo_CAN', 'jobInfo_CHE', 'jobInfo_CHL', 'jobInfo_CHN', 'jobInfo_COL', 'jobInfo_contingent worker', 'jobInfo_CZE', 'jobInfo_DEU', 'jobInfo_DNK', 'jobInfo_EGY', 'jobInfo_ESP', 'jobInfo_FIN', 'jobInfo_FRA', 'jobInfo_GBR', 'jobInfo_GTM', 'jobInfo_HKG', 'jobInfo_HUN', 'jobInfo_IDN', 'jobInfo_IND', 'jobInfo_ITA', 'jobInfo_JPN', 'jobInfo_KOR', 'jobInfo_LKA', 'jobInfo_MEX', 'jobInfo_MYS', 'jobInfo_NLD', 'jobInfo_NOR', 'jobInfo_NZL', 'jobInfo_OMN', 'jobInfo_PER', 'jobInfo_PHL', 'jobInfo_POL', 'jobInfo_PRT', 'jobInfo_QAT', 'jobInfo_ROU', 'jobInfo_RUS', 'jobInfo_SAU', 'jobInfo_SGP', 'jobInfo_SWE', 'jobInfo_THA', 'jobInfo_TUR', 'jobInfo_TWN', 'jobInfo_USA', 'jobInfo_VEN', 'jobInfo_VNM', 'jobInfo_ZAF', 'jobRelationsInfo', 'nationalIdCard', 'nationalIdCard_ARE', 'nationalIdCard_ARG', 'nationalIdCard_AUS', 'nationalIdCard_AUT', 'nationalIdCard_BEL', 'nationalIdCard_BGD', 'nationalIdCard_BRA', 'nationalIdCard_CAN', 'nationalIdCard_CHE', 'nationalIdCard_CHL', 'nationalIdCard_CHN', 'nationalIdCard_COL', 'nationalIdCard_CZE', 'nationalIdCard_DEU', 'nationalIdCard_DNK', 'nationalIdCard_EGY', 'nationalIdCard_ESP', 'nationalIdCard_FIN', 'nationalIdCard_FRA', 'nationalIdCard_GBR', 'nationalIdCard_GTM', 'nationalIdCard_HKG', 'nationalIdCard_HUN', 'nationalIdCard_IDN', 'nationalIdCard_IND', 'nationalIdCard_IRL', 'nationalIdCard_ITA', 'nationalIdCard_JPN', 'nationalIdCard_KOR', 'nationalIdCard_LKA', 'nationalIdCard_MAC', 'nationalIdCard_MEX', 'nationalIdCard_MYS', 'nationalIdCard_NLD', 'nationalIdCard_NOR', 'nationalIdCard_NZL', 'nationalIdCard_OMN', 'nationalIdCard_PER', 'nationalIdCard_PHL', 'nationalIdCard_POL', 'nationalIdCard_PRT', 'nationalIdCard_QAT', 'nationalIdCard_ROU', 'nationalIdCard_RUS', 'nationalIdCard_SAU', 'nationalIdCard_SGP', 'nationalIdCard_SWE', 'nationalIdCard_THA', 'nationalIdCard_TUR', 'nationalIdCard_TWN', 'nationalIdCard_USA', 'nationalIdCard_VEN', 'nationalIdCard_VNM', 'nationalIdCard_ZAF', 'payComponentNonRecurring', 'payComponentRecurring', 'paymentInfo', 'pensionPayoutsInfo', 'personalInfo', 'personalInfo_contingent worker', 'personInfo', 'personInfo_contingent worker', 'personInfo_employee', 'personRelationshipInfo', 'phoneInfo', 'userAccountInfo', 'workPermitInfo']
filter = Filter(Unfilter_list)
filter.filter_list()
filterDict = filter.create_dict()
filter.show_dict(filterDict)



    