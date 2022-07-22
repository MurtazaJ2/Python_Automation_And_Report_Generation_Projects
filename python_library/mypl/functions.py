import xml.etree.ElementTree as ET


class Connect_Jenkins:

    def __init__(self, config_xml_path):
        self.__config_xml_path = config_xml_path
        self.tree = ET.parse(self.__config_xml_path)
        self.root = self.tree.getroot()

    def update(self):
        self.tree.write(self.__config_xml_path)

    def filter_data(self):
        file = open(self.__config_xml_path, "r")
        content = file.read()
        replaced_str = content.replace(f"<publishers><", f"<publishers>")
        final_replaced_str = replaced_str.replace(f"/></publishers>", f" </publishers>")
        replaced_str1 = final_replaced_str.replace(f"<builders><", f"<builders>")
        final_replaced_str1 = replaced_str1.replace(f"/></builders>", f" </builders>")
        replaced_str2 = final_replaced_str1.replace(f"<buildWrappers><", f"<buildWrappers>")
        final_replaced_str2 = replaced_str2.replace(f"/></buildWrappers>", f" </buildWrappers>")
        final_replaced_str3 = final_replaced_str2.replace("/></parameterDefinitions>", "     </parameterDefinitions>")
        filtered_data3 = final_replaced_str3.replace("  <\n", "")
        filtered_data4 = filtered_data3.replace("      <\n", "")
        filtered_data5 = filtered_data4.replace(" /><\n", "")
        filtered_data2 = filtered_data5.replace("</parameterDefinitions>", " </parameterDefinitions>")
        filtered_data = filtered_data2.replace("/></properties>", " </properties>")
        file.close()
        with open(self.__config_xml_path, "w") as updated_file:
            updated_file.write(filtered_data)

    def replace_artifacts(self, change_artifacts):
        for parent in self.root.iter("artifacts"):
            try:
                change = change_artifacts
                parent.text = str(change)
                self.update()
            except ValueError:
                pass

    def edit_artifacts(self, edit_artifacts):
        for parent in self.root.iter("artifacts"):
            try:
                change = str(parent.text) + ", " + edit_artifacts
                parent.text = str(change)
                self.update()
            except ValueError:
                pass

    def add_artifacts(self, parent_tag, value, exclude="", emptyarchive=False, ifsuccessfull=False, fingerprint=False,
                      defaultexcludes=True, casesensitive=True, symlinks=False):
        element = self.tree.find('.//artifacts')
        if element is None:
            for parent in self.root.iter(parent_tag):
                try:
                    ET.SubElement(parent, (f"\n    <hudson.tasks.ArtifactArchiver>\n"
                                           f"        <artifacts>{value}</artifacts>\n"
                                           f"        <excludes>{exclude}</excludes>\n"
                                           f"        <allowEmptyArchive>{emptyarchive}</allowEmptyArchive>\n"
                                           f"        <onlyIfSuccessful>{ifsuccessfull}</onlyIfSuccessful>\n"
                                           f"        <fingerprint>{fingerprint}</fingerprint>\n"
                                           f"        <defaultExcludes>{defaultexcludes}</defaultExcludes>\n"
                                           f"        <caseSensitive>{casesensitive}</caseSensitive>\n"
                                           f"        <followSymlinks>{symlinks}</followSymlinks>\n"
                                           f"      </hudson.tasks.ArtifactArchiver>\n"))
                except ValueError:
                    pass
            self.update()
            self.filter_data()

        else:
            self.replace_artifacts(value)

    def add_copy_artifacts(self, parent_tag, project, selector="StatusBuildSelector", buildnumber="", parameters="",
                           filter="", target="", excludes="",
                           fingerprintartifacts=False, flatten=False, optional=False, variablesuffix="", stable=False):
        for parent in self.root.iter(parent_tag):
            try:
                ET.SubElement(parent, (f"\n    <hudson.plugins.copyartifact.CopyArtifact plugin=\"copyartifact@1.46.4\">\n"
                                       f"          <project>{project}</project>\n"
                                       f"          <parameters>{parameters}</parameters>\n"
                                       f"          <filter>{filter}</filter>\n"
                                       f"          <target>{target}</target>\n"
                                       f"          <excludes>{excludes}</excludes>\n"
                                       f"          <selector class=\"hudson.plugins.copyartifact.{selector}\">\n"
                                       f"             <stable>{stable}</stable>\n"
                                       f"             <buildNumber>{buildnumber}</buildNumber>\n"
                                       f"          </selector>\n"
                                       f"          <flatten>{flatten}</flatten>\n"
                                       f"          <optional>{optional}</optional>\n"
                                       f"          <doNotFingerprintArtifacts>{fingerprintartifacts}</doNotFingerprintArtifacts>\n "
                                       f"          <resultVariableSuffix>{variablesuffix}</resultVariableSuffix>\n"
                                       f"      </hudson.plugins.copyartifact.CopyArtifact>\n"))
            except ValueError:
                pass
        self.update()
        self.filter_data()

    def add_parameters(self, parent_tag, parameter_type, name="", defaultvalue="", description="", choices=""):
        element = self.tree.find('.//parameterDefinitions')
        if element is None:
            for parent in self.root.iter(parent_tag):
                try:
                    if parameter_type == "multiline string parameter":
                        ET.SubElement(parent, (f"\n    <hudson.model.ParametersDefinitionProperty>\n"
                                               f"         <parameterDefinitions>\n"
                                               f"            <hudson.model.TextParameterDefinition>\n"
                                               f"              <name>{name}</name>\n"
                                               f"              <description>{description}</description>\n"
                                               f"              <defaultValue>{defaultvalue}</defaultValue>\n"
                                               f"              <trim>false</trim>\n"
                                               f"            </hudson.model.TextParameterDefinition>\n"
                                               f"         </parameterDefinitions>\n"
                                               f"     </hudson.model.ParametersDefinitionProperty>\n"))

                    elif parameter_type == "choice parameter":
                        ET.SubElement(parent, (f"\n    <hudson.model.ParametersDefinitionProperty>\n"
                                               f"      <parameterDefinitions>\n"
                                               f"        <hudson.model.ChoiceParameterDefinition>\n"
                                               f"          <name>{name}</name>\n"
                                               f"          <description>{description}</description>\n"
                                               f"          <choices class=\"java.util.Arrays$ArrayList\">\n"
                                               f"            <a class=\"string-array\">\n"
                                               f"              <string>{choices}</string>\n"
                                               f"            </a>\n"
                                               f"          </choices>\n"
                                               f"        </hudson.model.ChoiceParameterDefinition>\n"
                                               f"      </parameterDefinitions>\n"
                                               f"    </hudson.model.ParametersDefinitionProperty>\n"))

                    # elif parameter_type == ""
                except ValueError:
                    pass
            self.update()
            self.filter_data()

        else:
            for parent in self.root.iter("parameterDefinitions"):
                try:
                    if parameter_type == "multiline string parameter":
                        ET.SubElement(parent, (f"\n     <hudson.model.TextParameterDefinition>\n"
                                               f"               <name>{name}</name>\n"
                                               f"               <description>{description}</description>\n"
                                               f"               <defaultValue>{defaultvalue}</defaultValue>\n"
                                               f"               <trim>false</trim>\n"
                                               f"            </hudson.model.TextParameterDefinition>\n"))

                    elif parameter_type == "choice parameter":
                        ET.SubElement(parent, (f"\n    <hudson.model.ChoiceParameterDefinition>\n"
                                               f"           <name>{name}</name>\n"
                                               f"           <description>{description}</description>\n"
                                               f"           <choices class=\"java.util.Arrays$ArrayList\">\n"
                                               f"             <a class=\"string-array\">\n"
                                               f"               <string>{choices}</string>\n"
                                               f"             </a>\n"
                                               f"           </choices>\n"
                                               f"        </hudson.model.ChoiceParameterDefinition>\n"))
                except ValueError:
                    pass
            self.update()
            self.filter_data()

    def remove_build_triggers(self, built_trigger):
        if built_trigger == "trigger builds remotely":
            for element in self.root.iter("authToken"):
                self.root.remove(element)
            self.update()
        elif built_trigger == "build after other projects are built":
            for parent in self.root.iter("triggers"):
                for child in parent.iter("jenkins.triggers.ReverseBuildTrigger"):
                    parent.remove(child)
            self.update()
        elif built_trigger == "build periodically":
            for parent in self.root.iter("triggers"):
                for child in parent.iter("hudson.triggers.TimerTrigger"):
                    parent.remove(child)
            self.update()
        elif built_trigger == "build when a change is pushed to gitLab":
            for parent in self.root.iter("triggers"):
                for child in parent.iter("com.dabsquared.gitlabjenkins.GitLabPushTrigger"):
                    parent.remove(child)
            self.update()
        elif built_trigger == "github hook trigger for gitscm polling":
            for parent in self.root.iter("triggers"):
                for child in parent.iter("com.cloudbees.jenkins.GitHubPushTrigger"):
                    parent.remove(child)
            self.update()
        elif built_trigger == "poll scm":
            for parent in self.root.iter("triggers"):
                for child in parent.iter("hudson.triggers.SCMTrigger"):
                    parent.remove(child)
            self.update()
        else:
            print("No such triggers")

    def check_build_environment(self):
        element = self.tree.find('.//hudson.plugins.ws__cleanup.PreBuildCleanup')
        if element is None:
            for parent in self.root.iter("buildWrappers"):
                try:
                    ET.SubElement(parent, (f"\n   <hudson.plugins.ws__cleanup.PreBuildCleanup plugin=\"ws-cleanup@0.42\">\n"
                                           f"      <patterns>\n"
                                           f"        <hudson.plugins.ws__cleanup.Pattern>\n"
                                           f"          <pattern></pattern>\n"
                                           f"          <type>INCLUDE</type>\n"
                                           f"        </hudson.plugins.ws__cleanup.Pattern>\n"
                                           f"      </patterns>\n"
                                           f"      <deleteDirs>false</deleteDirs>\n"
                                           f"      <cleanupParameter></cleanupParameter>\n"
                                           f"      <externalDelete></externalDelete>\n"
                                           f"      <disableDeferredWipeout>false</disableDeferredWipeout>\n"
                                           f"    </hudson.plugins.ws__cleanup.PreBuildCleanup>\n"
                                           f'    <hudson.plugins.timestamper.TimestamperBuildWrapper plugin="timestamper@1.17"/>\n'))
                except ValueError:
                    pass
        self.update()
        self.filter_data()

    def email_notification(self, email, unstablebuild=False, individuals=False):
        element = self.tree.find('.//hudson.tasks.Mailer')
        if element is None:
            for parent in self.root.iter("publishers"):
                try:
                    ET.SubElement(parent, (f"\n    <hudson.tasks.Mailer plugin=\"mailer@414.vcc4c33714601\">\n"
                                           f"      <recipients>{email}</recipients>\n"
                                           f"      <dontNotifyEveryUnstableBuild>{unstablebuild}</dontNotifyEveryUnstableBuild>\n"
                                           f"      <sendToIndividuals>{individuals}</sendToIndividuals>\n"
                                           f"    </hudson.tasks.Mailer>\n"))
                except ValueError:
                    pass
        self.update()
        self.filter_data()

    def execute_shell(self, parent_tag, command, retainvariables="", retain=True, variable_handling="", unstablereturn=""):
        for parent in self.root.iter(parent_tag):
            try:
                ET.SubElement(parent, (f"\n    <hudson.tasks.Shell>\n"
                                       f"      <command>{command}</command>\n"
                                       f"      <configuredLocalRules>\n"
                                       f"        <jenkins.tasks.filters.impl.RetainVariablesLocalRule>\n"
                                       f"          <variables>{retainvariables}</variables>\n"
                                       f"          <retainCharacteristicEnvVars>{retain}</retainCharacteristicEnvVars>\n"
                                       f"          <processVariablesHandling>{variable_handling}</processVariablesHandling>\n"
                                       f"        </jenkins.tasks.filters.impl.RetainVariablesLocalRule>\n"
                                       f"      </configuredLocalRules>\n"
                                       f"      <unstableReturn>{unstablereturn}</unstableReturn>\n"
                                       f"    </hudson.tasks.Shell>\n"))
            except ValueError:
                pass
        self.update()
        self.filter_data()

    def discard_old_builds(self, days="", numbers="", artifactdays="", artifactnumber=""):
        element = self.tree.find('.//jenkins.model.BuildDiscarderProperty')
        if element is None:
            for parent in self.root.iter("properties"):
                try:
                    ET.SubElement(parent, (f"\n    <jenkins.model.BuildDiscarderProperty>\n"
                                           f"      <strategy class=\"hudson.tasks.LogRotator\">\n"
                                           f"        <daysToKeep>{days}</daysToKeep>\n"
                                           f"        <numToKeep>{numbers}</numToKeep>\n"
                                           f"        <artifactDaysToKeep>{artifactdays}</artifactDaysToKeep>\n"
                                           f"        <artifactNumToKeep>{artifactnumber}</artifactNumToKeep>\n"
                                           f"      </strategy>\n"
                                           f"    </jenkins.model.BuildDiscarderProperty>\n"))
                except ValueError:
                    pass
        self.update()
        self.filter_data()
