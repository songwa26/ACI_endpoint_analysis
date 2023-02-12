import logging
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
event_db={}
with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/lab_epmc_111_2.3.log') as f:
    for line in f:
        # #---------------------------- new EP local learning start -----------------------------------#
        # if 'optype ADD' in line:
        #     # timestamp=line.split(': : ')[0].split(' ')[1][0:23]
        #     # logger.debug(f'当前的时间戳为{timestamp}')
        #     # logger.debug(f'当前的log为:{line},"optype ADD')
        #     flag=1
        #     # print(line)
        #
        # if 'epmc_process_ep_add'  in line or 'epmc_process_l3_upd' in line:
        #     if flag==1:
        #         event+=1
        #         EP_raw_data.append('annotation:local learned a new EP.')
        #
        #         with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
        #             w.write(json.dumps(EP_raw_data))
        #             w.write('\r\n')
        #         EP_raw_data = []
        #         flag = 0
        # if flag==1:
        #     EP_raw_data.append(line)
        #     event_db[event] = EP_raw_data
        # # ----------------------------new EP local learning end -----------------------------------#

        # #---------------------------- new EP local timeout start -----------------------------------#
        # if 'optype DEL' in line:
        #     flag = 1
        # if 'epmc_delete_ep' in line:
        #     if flag==1:
        #         event+=1
        #         EP_raw_data.append('annotation:EP timeout.')
        #
        #         with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
        #             w.write(json.dumps(EP_raw_data))
        #             w.write('\r\n')
        #         EP_raw_data = []
        #         flag = 0
        # if flag==1:
        #     EP_raw_data.append(line)
        #     event_db[event] = EP_raw_data
        #
        # #---------------------------- new EP local timeout end -----------------------------------#


        #---------------------------- learn new remote MAC start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:474: ADD:MAC Xr' in line:
            flag = 1
            EP_raw_data.append('annotation:learned new remote mac.')
        if 'epmc_process_ep_add' in line:
            if flag==1:
                # event+=1
                # EP_raw_data.append('annotation:learned new remote mac.')
                # print(EP_raw_data)
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)
            # event_db[event] = EP_raw_data

        #---------------------------- learn new remote MAC end -----------------------------------#



        #---------------------------- learn new remote IP start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:493: ADD:IP Xr' in line:
            flag = 1
            EP_raw_data.append('annotation:learned new remote IP.')
        # if 'epmc_process_ep_add' in line:
        #     if flag==1:
        #         # event+=1
        #         # EP_raw_data.append('annotation:learned new remote IP.')
        #         with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
        #             w.write(json.dumps(EP_raw_data))
        #             w.write('\r\n')
        #         EP_raw_data = []
        #         flag = 0
        if flag==1:
            EP_raw_data.append(line)
            # event_db[event] = EP_raw_data

        #---------------------------- learn new remote IP end -----------------------------------#


        # #---------------------------- learn new remote EP start -----------------------------------#
        # if 'epmc_debug_dump_xr_ep_req:474: ADD:MAC Xr' in line:
        #     flag = 1
        # if 'epmc_process_ep_add' in line:
        #     if flag==1:
        #         event+=1
        #         EP_raw_data.append('annotation:learn new remote EP.')
        #
        #         with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
        #             w.write(json.dumps(EP_raw_data))
        #             w.write('\r\n')
        #         EP_raw_data = []
        #         flag = 0
        # if flag==1:
        #     EP_raw_data.append(line)
        #     event_db[event] = EP_raw_data
        #
        # #---------------------------- learn new remote EP end -----------------------------------#



with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data') as f:
    for line in f:
        result = ''
        mac = ''
        ip = ''
        annotation = ''
        # timestamp = line.split(': ')[0].split(' ')[1]
        number=line.split(': ')[0].split(' ')[0]
        if 'optype ADD'  in line or 'optype DEL' in line:
            pattern_mac = "; MAC {mac};"
            results_mac = search(pattern_mac, line)
            mac=(results_mac['mac'])
        if 'ADD:MAC Xr ' in line:
            pattern_mac = 'ADD:MAC Xr ={mac}\\n'
            results_mac = search(pattern_mac, line)
            mac = (results_mac['mac'])
        if  'ADD:IP Xr' in line:
            pattern_ip = 'ADD:IP Xr ={ip}\\n'
            results_ip = search(pattern_ip, line)
            ip = results_ip['ip']

        if 'ip[' in line:
            pattern_ip = "ip[0] {ip};"
            results_ip = search(pattern_ip, line)
            ip=results_ip['ip']
        if 'annotation:' in line:
            pattern_annotation='annotation:{annotation}.", "{number}.{timestamp}: '
            results_annotation = search(pattern_annotation, line)
            annotation=results_annotation['annotation']
            number=results_annotation['number']
            timestamp=results_annotation['timestamp']
        # if '["' in line:
        #     pattern_number= '["{number}.'
        #     results_number = search(pattern_number, line)
        #     number=results_number['number']

        result=(f'{number:<10}{timestamp:<40}{mac:<20}{ip:<20}{annotation}')
        with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_result', 'a+') as w:
            w.write(result)
            w.write('\r\n')



