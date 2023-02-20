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

file1='/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/endpoint/endpoint_ip_to_mac_move_case/binlog_uuid_472_epmc_vdc_1_sub_1_level_3-DECODED'
with open(file1) as f:
    for line in f:
        #---------------------------- new  local EP learning start -----------------------------------#
        if 'optype ADD' in line:
            EP_raw_data.append('annotation:local learned a new EP.')
            flag=1
        if 'epmc_sdk_prog_l3_entry' in line or 'epmc_sdk_l2_entry_create' in line:
            if flag==1:
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        # ----------------------------new local EP learning end -----------------------------------#


        #---------------------------- new EP local timeout start -----------------------------------#
        if 'optype DEL' in line:
            flag = 1
            EP_raw_data.append('annotation:local EP timeout.')
        if 'epmc_delete_ep' in line:
            if flag==1:
                # EP_raw_data.append('annotation:local EP timeout.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #---------------------------- new EP local timeout end -----------------------------------#


        #---------------------------- learn new remote MAC start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:474: ADD:MAC Xr' in line:
            flag = 1
            EP_raw_data.append('annotation:learned new remote mac.')
        if 'EPM EP MAC key' in line:
            if flag==1:
                # EP_raw_data.append('annotation:learned new remote mac.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)
        #---------------------------- learn new remote MAC end -----------------------------------#



        #---------------------------- learn new remote IP start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:493: ADD:IP Xr' in line:
            flag = 1
            EP_raw_data.append('annotation:learned new remote IP.')
        if 'EPM EP IPV4 key' in line:
            if flag==1:
                # EP_raw_data.append('annotation:learned new remote IP.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)
            # event_db[event] = EP_raw_data

        #---------------------------- learn new remote IP end -----------------------------------#


        #---------------------------- remote IP timeout start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:493: DEL:IP Xr' in line:
            flag = 1
            EP_raw_data.append('annotation:remote IP timeout.')
        if 'epmc_sdk_l3_entry_delete' in line:
            if flag==1:
                # EP_raw_data.append('annotation:remote IP timeout.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        #---------------------------- remote IP timeout start-----------------------------------#

        #---------------------------- remote MAC timeout start -----------------------------------#
        if 'epmc_debug_dump_xr_ep_req:474: DEL:MAC Xr' in line:
            flag = 1
            EP_raw_data.append('annotation:remote MAC timeout.')
        if 'epmc_sdk_l2_entry_delete' in line:
            if flag==1:
                # EP_raw_data.append('annotation:remote MAC timeout.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        #---------------------------- remote MAC timeout -----------------------------------#


        #----------------------------IP bounce entry start -----------------------------------#
        if 'flags = bounce|IP' in line:
            flag = 1
            EP_raw_data.append('annotation:bounce entry.')
        if 'epmc_ep_age_add_opts' in line:
            if flag==1:
                # EP_raw_data.append('annotation:bounce entry.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #----------------------------IP bounce entry end-----------------------------------#

        #----------------------------IP bounce entry timeout start -----------------------------------#
        if 'epmc_sdk_ep_tables_del_bounce_flag' in line:
            flag = 1
            EP_raw_data.append('annotation:bounce entry timeout.')
        if 'epmc_ep_age_handle_bounce_expire' in line:
            if flag==1:
                # EP_raw_data.append('annotation:bounce entry timeout.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)

        #----------------------------IP bounce entry timeout-----------------------------------#

#----------------------------MAC bounce entry start -----------------------------------#
        if 'flags = bounce|MAC' in line:
            flag = 1
            EP_raw_data.append('annotation:MAC bounce entry.')
        if 'epmc_handle_ep_bounce' in line:
            if flag==1:
                # EP_raw_data.append('annotation:MAC bounce entry.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
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
            EP_raw_data.append('annotation:IP to MAC move.')
        if 'epmc_process_l3_upd' in line:
            if flag==1:
                # EP_raw_data.append('annotation:IP to MAC move.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #----------------------------IP to MAC move timeout-----------------------------------#


with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data') as f:
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
        # if '["' in line:
        pattern_1 = '["annotation:{annotation}.", "{number}. {timestamp}: '
        results_1 = search(pattern_1, line)
        # pattern_annotation='annotation:{annotation}.'
        # results_annotation = search(pattern_annotation, line)
        number = results_1['number']
        timestamp = results_1['timestamp']
        annotation=results_1['annotation']
        result=(f'{number:<10}{timestamp:<40}{mac:<20}{ip:<20}{annotation}')
        with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_result', 'a+') as w:
            w.write(result)
            w.write('\r\n')



