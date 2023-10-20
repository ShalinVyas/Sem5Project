import csv
from dateutil.parser import isoparse
import matplotlib.pyplot as plt
import seaborn as sns
import win32evtlog
import xml.etree.ElementTree as ET
import ctypes
import sys
import pandas as pd
import pprint
import subprocess

from pandas import DataFrame


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():

    # open event file
    query_handle = win32evtlog.EvtQuery(
        './apps.evtx',
        win32evtlog.EvtQueryFilePath)

    read_count = 0
    sources = []
    events_id = []
    times = []

    while True:
        # read 1 record(s)
        events = win32evtlog.EvtNext(query_handle, 10)
        read_count += len(events)
        # if there is no record break the loop
        if len(events) == 0:
            break
        for event in events:
            xml_content = win32evtlog.EvtRender(event, win32evtlog.EvtRenderEventXml)
            # parse xml content
            xml = ET.fromstring(xml_content)

            # xml namespace, root element has a xmlns definition, so we have to use the namespace
            ns = '{http://schemas.microsoft.com/win/2004/08/events/event}'
            if len(xml) > 1 and len(xml[1]) > 9:
                substatus = xml[1][9].text
            else:
                substatus = 'N/A'
            provider = xml.find(f'.//{ns}Provider')
            source = provider.get('Name')
            event_record_id = xml.find(f'.//{ns}EventRecordID').text
            event_id = xml.find(f'.//{ns}EventID').text
            computer = xml.find(f'.//{ns}Computer').text
            execution = xml.find(f'.//{ns}Execution')
            process_id = execution.get('ProcessID')
            thread_id = execution.get('ThreadID')
            time_created = xml.find(f'.//{ns}TimeCreated').get('SystemTime')
            # event_name = lookup_event_name(event_record_id)
            # data_name = xml.findall('.//EventData')
            # substatus = data_name.get('Data')
            # print(substatus)
            # print(source.group())

            sources.append(source)
            events_id.append(event_id)
            times.append(time_created)

            event_data = f'Source:{source},EventRecordID: {event_record_id}, Time: {time_created}, Computer: {computer}, Substatus: {substatus}, Event Id: {event_id}, Process Id: {process_id}, Thread Id: {thread_id}'
            df: DataFrame = pd.DataFrame({'Source': sources, 'Event ID': events_id, 'Time Created': times})
            # print(df)
            # print(event_data)
            df.to_csv("application.csv", index=False)
            output_file = "./application.csv"
            df['Date'] = pd.to_datetime(df['Time Created']).dt.strftime('%Y-%m-%d')
            df['Time'] = pd.to_datetime(df['Time Created']).dt.strftime('%H:%M:%S.%f')
            df.to_csv(output_file, index=False)
            # pprint.pprint(df)
            user_data = xml.find(f'.//{ns}UserData')

            # user_data has possible any data

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
