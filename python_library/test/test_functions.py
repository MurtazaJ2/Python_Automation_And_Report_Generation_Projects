from mypl import functions

change = functions.Connect_Jenkins("/home/murtaza/.jenkins/jobs/my_third_project/config.xml")
# change.add_parameters("properties", "multiline string parameter", name="project_demo2", choices="project value2", description="this is choice parameter")
# change.add_artifacts("publishers", "*.docx")
# change.add_copy_artifacts("builders", "project name")
# change.remove_build_triggers("Build after other projects are built")
# change.check_build_environment()
# change.email_notification("abc@gmail.com", unstablebuild=True)
# change.execute_shell("builders", 'echo "through python"')
change.discard_old_builds(days="515", numbers="3233")