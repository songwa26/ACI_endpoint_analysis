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
            EP_raw_data = []
            EP_raw_data.append('annotation1:local learned a new EP.')
            flag=1
        if 'Adding HT timer for' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
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
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:local EP timeout.')
        if 'epmc_delete_ep' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
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
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:learned new remote mac.')
        if 'Adding Age timer for' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
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
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:learned new remote IP.')
        if 'Adding Age timer for' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
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
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:remote MAC timeout.')
        if 'epmc_sdk_l2_entry_delete' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
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
            EP_raw_data = []
            flag = 1
            EP_raw_data.append('annotation1:bounce entry timeout.')
        if 'epmc_ep_age_handle_bounce_expire' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2: .')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
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
            EP_raw_data = []
            EP_raw_data.append('annotation1:N/A.')
        if 'moved from MAC' in line:
            if flag==1:
                EP_raw_data.append(line)
                EP_raw_data.append('annotation2:| IP to MAC move.')
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
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
                with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_raw_data', 'a+') as w:
                    w.write(json.dumps(EP_raw_data))
                    w.write('\r\n')
                EP_raw_data = []
                flag = 0
        if flag==1:
            EP_raw_data.append(line)


        #----------------------------EP move local end-----------------------------------#


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
        with open('/Users/songwa/PycharmProjects/pythonProject/venv/EPM analysis/epmc_result', 'a+') as w:
            w.write(result)
            w.write('\r\n')

