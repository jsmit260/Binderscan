import math
import json
import random

num_of_builds = 299 # % of utility Class B 
amis = [
'ami-09a41e26df464c548', #debian11
'ami-08c40ec9ead489470', #ubuntu 22.04 LTS
'ami-08e167817c87ed7fd', #SUSE Linux 
'ami-0a115baff5798ce9f', #Microsoft Windows Server 2012 R2 Base
'ami-06640050dc3f556bb', #Red Hat Enterprise Linux 8 
'ami-09d3b3274b6c5d4aa', #Amazon Linux 2 AMI - Kernel 5.10
'ami-0c4e4b4eb2e11d1d4', #Amazon Linux 2 AMI - Kernel 4.14
'ami-0149b2da6ceec4bb0', #Different Ubuntu Server 20.04 LTS 
'ami-017cdd6dc706848b2', #Microsoft Windows Server 2022 Base
'ami-02391c0e9583c17f7', #Microsoft Windows Server 2022 Core Base
'ami-026bb75827bd3d68d', #Microsoft Windows Server 2019 Base
'ami-0f3a1c7abf69a156d', #Microsoft Windows Server 2019 Core Base
'ami-049491187e7fcac1f', #Microsoft Windows Server 2016 Base
'ami-0e604dba9d44657a3', #Microsoft Windows Server 2016 Core Base
'ami-0b97110ce9fc52361', #SUSE Linux Enterprise Server 12 SP5 
'ami-0a115baff5798ce9f', #Microsoft Windows Server 2012 R2 Base
'ami-005b11f8b84489615', #Amazon Linux 2 with .NET 6, PowerShell, Mono, and MATE Desktop Environment
'ami-0ee23bfc74a881de5' #Ubuntu Server 18.04 LTS (HVM), SSD Volume Type
 ]
random_machine = random.choices(amis,k=num_of_builds)
for i in range(1,num_of_builds+1):
    resource = 'resource "aws_instance" "{}" {{\n\tami=\t"{}"\n\tinstance_type = "t2.micro"\n\tkey_name="aws_key"\n\t\tconnection{{\n\t\t\ttype="ssh"\n\t\t\thost=self.public_ip\n\t\t\tuser="ubuntu"\n\t\t\tprivate_key=file("root/.ssh/aws_key")\n\t\t\ttimeout="4m"\n\t}}\n}}'.format('b'+str(i),random_machine[i-1])
    print(resource)
    with open("auto_terraform_out.tf","a+") as f:
        f.write(resource+"\n")


