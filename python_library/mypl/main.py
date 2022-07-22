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

    if "copy artifacts" in section:
        copy_artifact = config["copy artifacts"]["copy artifact"]
        selector = config["copy artifacts"]["selector"]
        buildnumber = config["copy artifacts"]["buildnumber"]
        parameters = config["copy artifacts"]["parameters"]
        filter = config["copy artifacts"]["filter"]
        target = config["copy artifacts"]["target"]
        excludes = config["copy artifacts"]["excludes"]
        fingerprintartifacts = config["copy artifacts"]["fingerprintartifacts"]
        flatten = config["copy artifacts"]["flatten"]
        optional = config["copy artifacts"]["optional"]
        variablesuffix = config["copy artifacts"]["variablesuffix"]
        stable = config["copy artifacts"]["stable"]
        change.add_copy_artifacts("builders", copy_artifact, selector=selector, buildnumber=buildnumber,
                                  parameters=parameters,
                                  filter=filter, target=target, excludes=excludes,
                                  fingerprintartifacts=fingerprintartifacts, flatten=flatten, optional=optional,
                                  variablesuffix=variablesuffix, stable=stable)

    if "Build Environment" in section:
        change.check_build_environment()

    if "Execute shell" in section:
        shell = config["Execute shell"]["shell"]
        retainvariables = config["Execute shell"]["retainvariables"]
        retain = config["Execute shell"]["retain"]
        variable_handling = config["Execute shell"]["variable_handling"]
        unstablereturn = config["Execute shell"]["unstablereturn"]
        change.execute_shell("builders", shell, retainvariables=retainvariables, retain=retain,
                             variable_handling=variable_handling, unstablereturn=unstablereturn)
