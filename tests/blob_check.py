from logging import exception
import argparse
import os
import re
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from datetime import datetime
from pytz import timezone
import pandas as pd


list_of_dataframe = list()


def blob_storage_connect(container_name):
    try:
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(
            connect_str)
        # Instantiate a ContainerClient
        container_client = blob_service_client.get_container_client(
            container_name)
        blobs_list = container_client.list_blobs()
        return blobs_list
    except Exception as ex:
        print('Exception:')
        print(ex)


def cut_str(s, l):
    return [int(s[i:i+l]) for i in range(0, len(s), l)]


def strdate_to_datetime(str_date, str_time):
    _date = cut_str(str_date, 2)
    _date[0] += 2000
    _time = cut_str(str_time, 2)
    return datetime(*_date, *_time)


def making_dataframe(col_dict):
    data_frame = pd.DataFrame([col_dict])
    return data_frame


def converting_df_to_excel(df, filename):
    return df.to_excel("{}.xlsx".format(filename), encoding='utf-8')


def filter_work(search_word, check_list):
    filtered_list = [x for x in check_list if re.match(search_word, x.name)]
    for idx, blob_attr in enumerate(filtered_list):
        if idx+1 == len(filtered_list):  # 마지막 원소
            watch_sn = blob_attr.name.split('/')[-1].split('_')[0]
            record_day_null_timezone = blob_attr.name.split(
                '/')[-1].split('_')[1]
            record_time_null_timezone = blob_attr.name.split(
                '/')[-1].split('_')[2]
            watch_datetime_datetime_null = strdate_to_datetime(
                record_day_null_timezone, record_time_null_timezone)

            # watch 가 중국시각대일때
            record_watch_china = timezone('Asia/Shanghai')

            # watch가 중국 시각대이라고 가정하고 계산
            record_watch_datetime_null = watch_datetime_datetime_null.astimezone(
                record_watch_china)
            str_record_watch_datetime = str(record_watch_datetime_null)

            # beacon 정보
            beacon_mac_addr_number_4 = blob_attr.name.split(
                '/')[-1].split('_')[-1].split('.')[0][8:12]

            # KST 시간대 설정
            uploaded_Time_UTC = blob_attr.last_modified
            KST = timezone('Asia/Seoul')
            uploaded_datetime_KST = uploaded_Time_UTC.astimezone(KST)
            str_uploaded_datetime_KST = str(uploaded_datetime_KST)
            upload_day_KST = str_uploaded_datetime_KST.split(' ')[0]
            upload_time_KST = str_uploaded_datetime_KST.split(
                ' ')[-1].split('+')[0]
            # China 시간대 설정
            China = timezone('Asia/Shanghai')
            uploaded_datetime_China = uploaded_Time_UTC.astimezone(China)
            str_uploaded_datetime_China = str(uploaded_datetime_China)
            upload_day_China = str_uploaded_datetime_China.split(' ')[0]
            upload_time_China = str_uploaded_datetime_China.split(
                ' ')[-1].split('+')[0]
            diff_time_calculation = uploaded_datetime_China - record_watch_datetime_null
            str_diff_time_calcutaion = str(diff_time_calculation)

            if not beacon_mac_addr_number_4:
                beacon_mac_addr_number_4 = 'null'
            else:
                pass

            dataframe_for_file = making_dataframe({'watch_number': watch_sn,
                                                   'str_record_watch_datetime': str_record_watch_datetime,
                                                   'record_day_null_timezone': record_day_null_timezone,
                                                   'record_time_null_timezone': record_time_null_timezone,
                                                   'beacon_mac_addr_number_4': beacon_mac_addr_number_4,
                                                   'str_uploaded_datetime_KST': str_uploaded_datetime_KST,
                                                   'upload_day_KST': upload_day_KST,
                                                   'upload_time_KST': upload_time_KST,
                                                   'str_uploaded_datetime_China': str_uploaded_datetime_China,
                                                   'upload_day_China': upload_day_China,
                                                   'upload_time_China': upload_time_China,
                                                   'str_diff_time_calcutaion': str_diff_time_calcutaion, })
            list_of_dataframe.append(dataframe_for_file)
            final_dataframe = pd.concat(
                list_of_dataframe).reset_index(drop=True)
            return final_dataframe

        else:
            watch_sn = blob_attr.name.split('/')[-1].split('_')[0]
            record_day_null_timezone = blob_attr.name.split(
                '/')[-1].split('_')[1]
            record_time_null_timezone = blob_attr.name.split(
                '/')[-1].split('_')[2]
            # str 타입을 datetime으로 변경

            watch_datetime_datetime_null = strdate_to_datetime(
                record_day_null_timezone, record_time_null_timezone)

            # watch 가 중국시각대일때
            record_watch_china = timezone('Asia/Shanghai')

            # watch가 중국 시각대이라고 가정하고 계산
            record_watch_datetime_null = watch_datetime_datetime_null.astimezone(
                record_watch_china)
            str_record_watch_datetime = str(record_watch_datetime_null)

            # beacon 정보
            beacon_mac_addr_number_4 = blob_attr.name.split(
                '/')[-1].split('_')[-1].split('.')[0][8:12]

            # KST 시간대 설정
            uploaded_Time_UTC = blob_attr.last_modified
            KST = timezone('Asia/Seoul')
            uploaded_datetime_KST = uploaded_Time_UTC.astimezone(KST)
            str_uploaded_datetime_KST = str(uploaded_datetime_KST)
            upload_day_KST = str_uploaded_datetime_KST.split(' ')[0]
            upload_time_KST = str_uploaded_datetime_KST.split(
                ' ')[-1].split('+')[0]
            # China 시간대 설정
            China = timezone('Asia/Shanghai')
            uploaded_datetime_China = uploaded_Time_UTC.astimezone(China)
            str_uploaded_datetime_China = str(uploaded_datetime_China)
            upload_day_China = str_uploaded_datetime_China.split(' ')[0]
            upload_time_China = str_uploaded_datetime_China.split(
                ' ')[-1].split('+')[0]
            diff_time_calculation = uploaded_datetime_China - record_watch_datetime_null
            str_diff_time_calcutaion = str(diff_time_calculation)

            if not beacon_mac_addr_number_4:
                beacon_mac_addr_number_4 = 'null'
            else:
                pass

            dataframe_for_file = making_dataframe({'watch_number': watch_sn,
                                                   'str_record_watch_datetime': str_record_watch_datetime,
                                                   'record_day_null_timezone': record_day_null_timezone,
                                                   'record_time_null_timezone': record_time_null_timezone,
                                                   'beacon_mac_addr_number_4': beacon_mac_addr_number_4,
                                                   'str_uploaded_datetime_KST': str_uploaded_datetime_KST,
                                                   'upload_day_KST': upload_day_KST,
                                                   'upload_time_KST': upload_time_KST,
                                                   'str_uploaded_datetime_China': str_uploaded_datetime_China,
                                                   'upload_day_China': upload_day_China,
                                                   'upload_time_China': upload_time_China,
                                                   'str_diff_time_calcutaion': str_diff_time_calcutaion, })
            list_of_dataframe.append(dataframe_for_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="smartwatch_upload_file_check")
    parser.add_argument(
        "blob_name", help="blob_name in the container", type=str)
    parser.add_argument("container_name", help="cotainer_name", type=str)
    parser.add_argument("save_filename", help="excel_file_name", type=str)

    args = parser.parse_args()

    excel_source = filter_work(
        args.blob_name, blob_storage_connect(args.container_name))
    converting_df_to_excel(excel_source, args.save_filename)
