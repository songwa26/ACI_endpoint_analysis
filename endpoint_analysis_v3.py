import logging
import datetime
from parse import *     # 使用parse捕获想要的字段
import json
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s : %(message)s")

logconsole=logging.StreamHandler()
logconsole.setFormatter(formatter)
logger=logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logconsole)

flag=0
event=0
EP_raw_data=[]
timestamp=str()

file1='/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/endpoint/endpoint_ip_to_mac_move_case/binlog_uuid_472_epmc_vdc_1_sub_1_level_3-DECODED'
EP_raw_data_file = '/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data'

with open(file1) as f:
    print('正在分析log，请稍等...')
    for line in f:
        #---------------------------- new  local EP learning start -----------------------------------#
        if 'optype ADD' in line:
            EP_raw_data = []
            EP_raw_data.append('annotation1:local learned a new EP.')
            flag=1
        if 'Adding HT timer for' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        # ----------------------------new local EP learning end -----------------------------------#


        #---------------------------- new EP local timeout start -----------------------------------#
        if 'optype DEL' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:local EP timeout.')
        if 'epmc_delete_ep' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #---------------------------- new EP local timeout end -----------------------------------#


        #---------------------------- learn new remote MAC start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:474: ADD:MAC Xr' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:learned new remote mac.')
        if 'Adding Age timer for' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)
        #---------------------------- learn new remote MAC end -----------------------------------#



        #---------------------------- learn new remote IP start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:493: ADD:IP Xr' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:learned new remote IP.')
        if 'Adding Age timer for' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        #---------------------------- learn new remote IP end -----------------------------------#


        #---------------------------- remote IP timeout start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:493: DEL:IP Xr' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:remote IP timeout.')
        if 'epmc_sdk_l3_entry_delete' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        #---------------------------- remote IP timeout start-----------------------------------#

        #---------------------------- remote MAC timeout start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:474: DEL:MAC Xr' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:remote MAC timeout.')
        if 'epmc_sdk_l2_entry_delete' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        #---------------------------- remote MAC timeout -----------------------------------#


        #----------------------------IP bounce entry start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:493: UPD:IP Xr' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:bounce entry.')
        if 'seconds from now and type is Bounce' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #----------------------------IP bounce entry end-----------------------------------#

        #----------------------------IP bounce entry timeout start -----------------------------------#
        if 'epmc_sdk_ep_tables_del_bounce_flag' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:bounce entry timeout.')
        if 'epmc_ep_age_handle_bounce_expire' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        #----------------------------IP bounce entry timeout-----------------------------------#

#----------------------------MAC bounce entry start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:474: UPD:MAC Xr' in line:
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:N/A.')
        if 'epmc_handle_ep_bounce' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2:MAC bounce entry.')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #----------------------------MAC bounce entry end-----------------------------------#


        #----------------------------IP to MAC move start -----------------------------------#
        if 'optype UPD;' in line:
            flag = 1
            EP_raw_data = []
            EP_raw_data.append('annotation1:N/A.')
        if 'moved from MAC' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2:| IP to MAC move.')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #----------------------------IP to MAC move timeout-----------------------------------#

       #----------------------------EP move local start -----------------------------------#
        if 'optype UPD;' in line:
            flag = 1
            EP_raw_data = []
            EP_raw_data.append('annotation1:N/A.')
        if 'Removing EP from IF idx 0x' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2:| EP move to local.')
                with open(EP_raw_data_file, 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #----------------------------EP move local end-----------------------------------#





def output(EP_raw_data_file,EP_result):
    with open(EP_raw_data_file) as f:
        for line in f:
            result = ''
            mac = ''
            ip = ''
            annotation = ''

            if 'optype ADD'  in line or 'optype DEL' in line:
                pattern_mac = "; MAC {mac};"
                results_mac = search(pattern_mac, line)
                mac=(results_mac['mac'])
            if 'optype UPD;'  in line:
                pattern_mac = "; MAC {mac};"
                results_mac = search(pattern_mac, line)
                mac=(results_mac['mac'])
            if 'ADD:MAC Xr ' in line:
                pattern_mac = 'ADD:MAC Xr = {mac}\\n'
                results_mac = search(pattern_mac, line)
                mac = (results_mac['mac'])
            if 'Process MAC' in line:
                pattern_mac = 'Process MAC {mac} update'
                results_mac = search(pattern_mac, line)
                mac = (results_mac['mac'])
            if 'DEL:MAC Xr' in line:
                pattern_mac = 'DEL:MAC Xr = {mac}\\n'
                results_mac = search(pattern_mac, line)
                mac = (results_mac['mac'])
            if 'ADD:IP Xr =' in line:
                pattern_ip = 'ADD:IP Xr = {ip}\\n'
                results_ip = search(pattern_ip, line)
                ip = results_ip['ip']
            if 'IP: ' in line:     # for bounce entry IP
                pattern_ip = 'IP: {ip}\\n'
                results_ip = search(pattern_ip, line)
                ip = results_ip['ip']
            if 'DEL:IP Xr =' in line:
                pattern_ip = 'DEL:IP Xr = {ip}\\n'
                results_ip = search(pattern_ip, line)
                ip = results_ip['ip']
            if 'UPD:IP Xr =' in line:
                pattern_ip = 'UPD:IP Xr = {ip}\\n'
                results_ip = search(pattern_ip, line)
                ip = results_ip['ip']
            if 'UPD:MAC Xr =' in line:
                pattern_mac = 'UPD:MAC Xr = {mac}\\n'
                results_mac = search(pattern_mac, line)
                mac = (results_mac['mac'])
            if 'ip[' in line:
                pattern_ip = "ip[0] {ip};"
                results_ip = search(pattern_ip, line)
                ip=results_ip['ip']

            if 'IF idx 0x' in line:
                pattern_interface = "IF idx {interface};"
                result_interface=search(pattern_interface, line)
                interface=result_interface['interface']

            if ' tun_if_idx = 0x'in line:
                pattern_interface = "tun_if_idx = {interface};"
                result_interface = search(pattern_interface, line)
                interface = result_interface['interface']

            if 'flags local' in line:
                pattern_flags = 'flags local{flags}|\\n'
                result_flags = search(pattern_flags, line)
                flags = result_flags['flags']
                flags='local'+flags

            if '; flags = ' in line:
                pattern_flags = '; flags = {flags}|;'
                result_flags = search(pattern_flags, line)
                flags = result_flags['flags']

            pattern = '["annotation1:{annotation1}.", "{number}. {timestamp}: {other}annotation2:{annotation2}.'
            results = search(pattern, line)
            number = results['number']
            timestamp = results['timestamp']
            annotation1=results['annotation1']
            annotation2=results['annotation2']
            result=(f'{number:<10}{timestamp:<40}{mac:<20}{ip:<20}{interface:<20}{flags:<50}{annotation1} {annotation2}')
            with open(EP_result, 'a+') as w:
                w.write(result)
                w.write('\r\n')


def function(EP_raw_data_file):
    function1=input('请输入想要的功能,1为输出全部log，2为过滤特定时间log:')
    # EP_raw_data = '/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data'
    if function1=='1':
        EP_result='/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_all_result'
        output(EP_raw_data_file,EP_result)

    if function1=='2':
        time_range = input('请输入指定时间范围（比如2023-01-31T11:13:31~2023-01-31T12:13:31):')
        time_start = time_range.split('~')[0]
        time_end = time_range.split('~')[1]
        time_start = datetime.datetime.strptime(time_start, "%Y-%m-%dT%H:%M:%S")
        time_end = datetime.datetime.strptime(time_end, "%Y-%m-%dT%H:%M:%S")
        EP_result_timerange_raw_data = '/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/EP_result_timerange_raw_data'
        EP_result_timerange = '/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/EP_result_timerange'
        with open(EP_raw_data_file) as f:
            print('正在分析log，请稍等...')
            for line in f:
                pattern = '["annotation1:{annotation1}.", "{number}. {timestamp}.'
                results = search(pattern, line)
                timestamp = results['timestamp']
                # print(timestamp)
                timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
                # print(time_start)
                # print(time_end)
                # print(timestamp)
                if timestamp > time_start and timestamp < time_end:
                    with open(EP_result_timerange_raw_data, 'a+') as w:
                        w.write(line)
                        # w.write('\r\n')
        output(EP_result_timerange_raw_data, EP_result_timerange)
        function2 = input('如果想要在这段时间内对指定endpoint做统计，请输入1，否则输入2中断脚本:')
        if function2 == '1':
            endpoint = input('请输入指定endpoint相关的log(比如0050.5686.9be4或10.164.3.221):')
            EP_result_timerange_endpoint=f'/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/EP_result_timerange_{endpoint}'
            # print(EP_result_timerange_endpoint)
            with open(EP_result_timerange) as f:
                for line in f:
                    if endpoint in line:
                        with open(EP_result_timerange_endpoint, 'a+') as w:
                            w.write(line)
            print('分析完成')
        elif function2 == '2':
            print('分析完成')

function(EP_raw_data_file)
