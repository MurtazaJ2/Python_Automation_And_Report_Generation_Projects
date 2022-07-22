import xml.etree.ElementTree as ET
import configparser


# def add_copy_artifacts(parent_tag, project, parameters="", filter="", target="", excludes="", FingerprintArtifacts=False, flatten=False, optional=False, variablesuffix="", stable=False):
#     tree = ET.parse("config.xml")
#     root = tree.getroot()
#     for child in root.iter(parent_tag):
#         nm = ET.SubElement(child, f"""\n    <hudson.plugins.copyartifact.CopyArtifact plugin="copyartifact@1.46.4">
#        <project>{project}</project>
#        <parameters>{parameters}</parameters>
#        <filter>{filter}</filter>
#        <target>{target}</target>
#        <excludes>{excludes}</excludes>
#        <selector class="hudson.plugins.copyartifact.StatusBuildSelector"/>
#         <stable>{stable}</stable>
#        </selector>
#        <flatten>{flatten}</flatten>
#        <optional>{optional}</optional>
#        <doNotFingerprintArtifacts>{FingerprintArtifacts}</doNotFingerprintArtifacts>
#        <resultVariableSuffix>{variablesuffix}</resultVariableSuffix>
#     </hudson.plugins.copyartifact.CopyArtifact>\n""")
#
#     tree.write("config.xml")
#     file = open("config1.xml", "r")
#     content = file.read()
#
#     f = content.replace(f"<{parent_tag}><", f"<{parent_tag}>")
#
#     d = f.replace(f"/></{parent_tag}>", f" </{parent_tag}>")
#     e = d.replace("  <\n","")
#
#     with open("config1.xml","w") as variable_name:
#         variable_name.write(e)

# def add_artifacts(parent_tag, value, exclude=None, emptyarchive=False, ifsuccessful=False, fingerprint=False, defaultexcludes=True, casesensitive=True, symlinks=False):
#     tree = ET.parse("config.xml")
#     root = tree.getroot()
#     all_name_elements = tree.find('.//artifacts')
#     if all_name_elements == None:
#         for child in root.iter(parent_tag):
#                 nm = ET.SubElement(child, f"""\n    <hudson.tasks.ArtifactArchiver>
#                 <artifacts>{value}</artifacts>
#                 <excludes>{exclude}</excludes>
#                 <allowEmptyArchive>{emptyarchive}</allowEmptyArchive>
#                 <onlyIfSuccessful>{ifsuccessful}</onlyIfSuccessful>
#                 <fingerprint>{fingerprint}</fingerprint>
#                 <defaultExcludes>{defaultexcludes}</defaultExcludes>
#                 <caseSensitive>{casesensitive}</caseSensitive>
#                 <followSymlinks>{symlinks}</followSymlinks>
#               </hudson.tasks.ArtifactArchiver>\n""")
#
#         tree.write("config.xml")
        # file = open("config1.xml", "r")
        # content = file.read()
        #
        # f = content.replace("<publishers><", "<publishers>")
        #
        # d = f.replace("/></publishers>", "</publishers>")
        #
        # with open("config1.xml","w") as variable_name:
        #     variable_name.write(d)

    # else:
    #     print("data already exists")

# def add_parameters(parent_tag, name="", defaultvalue="", description=""):
#     tree = ET.parse("config.xml")
#     root = tree.getroot()
#     all_name_elements = tree.find('.//parameterDefinitions')
#     if all_name_elements == None:
#         for child in root.iter(parent_tag):
#             nm = ET.SubElement(child, f"""\n    <hudson.model.ParametersDefinitionProperty>
#           <parameterDefinitions>
#             <hudson.model.TextParameterDefinition>
#               <name>{name}</name>
#               <description>{description}</description>
#               <defaultValue>{defaultvalue}</defaultValue>
#               <trim>false</trim>
#             </hudson.model.TextParameterDefinition>
#           </parameterDefinitions>
#         </hudson.model.ParametersDefinitionProperty>\n""")
#         tree.write("config.xml")
#         file = open("config1.xml", "r")
#         content = file.read()
#
#         f = content.replace(f"<{parent_tag}><", f"<{parent_tag}>")
#
#         d = f.replace(f"/></{parent_tag}>", f"</{parent_tag}>")
#         filtered_data = d.replace("  <\n", "")
#
#         with open("config1.xml","w") as variable_name:
#             variable_name.write(filtered_data)
#
#     else:
#         print("data already exists")

# def filter_data(parent_tag):
#     file = open("config1.xml", "r")
#     content = file.read()
#     replaced_str = content.replace(f"<{parent_tag}><", f"<{parent_tag}>")
#     final_replaced_str = replaced_str.replace(f"/></{parent_tag}>", f" </{parent_tag}>")
#     file.close()
#     with open("config1.xml", "w") as updated_file:
#         updated_file.write(final_replaced_str)

# def remove_build_triggers(built_trigger):
#     tree = ET.parse("config.xml")
#     root = tree.getroot()
    # if  built_trigger == "Trigger builds remotely":
    #     for child in root.iter("authToken"):
    #         print(child)
    #         root.remove(child)
    #     tree.write("config1.xml")
    # if built_trigger == "Build after other projects are built":
    #     for parent in root.iter("triggers"):
    #         for child in parent.iter("jenkins.triggers.ReverseBuildTrigger"):
    #             print(child)
    #             parent.remove(child)
    #     tree.write("config1.xml")
        # for parent in root.iter("authToken"):
        #     parent.remove(parent)
        # tree.write("config1.xml")
    # all_name_elements = tree.find('.//triggers')
    # if all_name_elements != None:
    #     for child in root.iter("triggers"):

# def check_build_environment():
#     tree = ET.parse("config1.xml")
#     root = tree.getroot()
#     element = tree.find('.//hudson.plugins.ws__cleanup.PreBuildCleanup')
#     if element is None:
#         for parent in root.iter("buildWrappers"):
#             ET.SubElement(parent, (f"\n   <hudson.plugins.ws__cleanup.PreBuildCleanup plugin=\"ws-cleanup@0.42\">\n"
#                                    f"      <patterns>\n"
#                                    f"        <hudson.plugins.ws__cleanup.Pattern>\n"
#                                    f"          <pattern></pattern>\n"
#                                    f"          <type>INCLUDE</type>\n"
#                                    f"        </hudson.plugins.ws__cleanup.Pattern>\n"
#                                    f"      </patterns>\n"
#                                    f"      <deleteDirs>false</deleteDirs>\n"
#                                    f"      <cleanupParameter></cleanupParameter>\n"
#                                    f"      <externalDelete></externalDelete>\n"
#                                    f"      <disableDeferredWipeout>false</disableDeferredWipeout>\n"
#                                    f"   </hudson.plugins.ws__cleanup.PreBuildCleanup>\n"
#                                    f'   <hudson.plugins.timestamper.TimestamperBuildWrapper plugin="timestamper@1.17"/>\n'))
#     else:
#         print("data already exists")
    # element = tree.find('.//hudson.plugins.timestamper.TimestamperBuildWrapper')
    # if element is None:
    #     for parent in root.iter("buildWrappers"):
    #         ET.SubElement(parent, '    <hudson.plugins.timestamper.TimestamperBuildWrapper plugin="timestamper@1.17"/>\n')
    # else:
    #     print("data already exists")
    # tree.write("config1.xml")
    # filter_data("buildWrappers")

# def email_notification(email, unstablebuild=False, individuals=False):
#     tree = ET.parse("config.xml")
#     root = tree.getroot()
#     element = tree.find('.//hudson.tasks.Mailer')
#     if element is None:
#         for parent in root.iter("publishers"):
#             ET.SubElement(parent, (f"\n    <hudson.tasks.Mailer plugin=\"mailer@414.vcc4c33714601\">\n"
#                                    f"      <recipients>{email}</recipients>\n"
#                                    f"      <dontNotifyEveryUnstableBuild>{unstablebuild}</dontNotifyEveryUnstableBuild>\n"
#                                    f"      <sendToIndividuals>{individuals}</sendToIndividuals>\n"
#                                    f"    </hudson.tasks.Mailer>\n"))
#     else:
#         print("data already exists")
#     tree.write("config1.xml")

# from mypl import functions
# from configparser import ConfigParser
#
# change = functions.Connect_Jenkins("/home/murtaza/.jenkins/jobs/my_third_project/config.xml")
# config = ConfigParser()
# config.read('config.ini')
# thedict = {}
# for section in config.sections():
#     thedict[section] = {}
#     for key,val in config.items(section):
#         thedict[section][key] = val
#         if val == "false":
#             change.remove_build_triggers(key)
#         else:
#             print(nothing)

# def filter_data(self, parent_tag):
#     file = open(self.__config_xml_path, "r")
#     content = file.read()
#     replaced_str = content.replace(f"<{parent_tag}><", f"<{parent_tag}>")
#     final_replaced_str = replaced_str.replace(f"/></{parent_tag}>", f" </{parent_tag}>")
#     final_replaced_str1 = final_replaced_str.replace("/></parameterDefinitions>", "     </parameterDefinitions>")
#     filtered_data1 = final_replaced_str1.replace("      <\n", "")
#     filtered_data2 = filtered_data1.replace("</parameterDefinitions>", "     </parameterDefinitions>")
#     filtered_data = filtered_data2.replace("  <\n", "")
#     file.close()
#     with open(self.__config_xml_path, "w") as updated_file:
#         updated_file.write(filtered_data)

from mypl import functions
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
location = config.get("Credentials", "location")
change = functions.Connect_Jenkins(location)
the_dict = {}

for section in config.sections():
    the_dict[section] = {}

    if "Build Triggers" in section:
        for key, value in config.items(section):
            the_dict[section][key] = value
        change.remove_build_triggers(key)

    if "publishers artifact" in section:
        artifacts = config["publishers artifact"]["artifacts"]
        exclude = config["publishers artifact"]["exclude"]
        emptyarchive = config["publishers artifact"]["emptyarchive"]
        ifsuccessfull = config["publishers artifact"]["ifsuccessfull"]
        fingerprint = config["publishers artifact"]["fingerprint"]
        defaultexcludes = config["publishers artifact"]["defaultexcludes"]
        casesensitive = config["publishers artifact"]["casesensitive"]
        symlinks = config["publishers artifact"]["symlinks"]
        change.add_artifacts("publishers", artifacts, exclude=exclude, emptyarchive=emptyarchive,
                             ifsuccessfull=ifsuccessfull, fingerprint=fingerprint,
                             defaultexcludes=defaultexcludes, casesensitive=casesensitive, symlinks=symlinks)