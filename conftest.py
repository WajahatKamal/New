
from pluggy import HookspecMarker

hookspec = HookspecMarker("pytest")
import os
import json


def pytest_bdd_before_scenario(feature, scenario):
    print("\n")
    print("---------------------------------------------------------------------------------------------")
    print("STARTED EXECUTION OF SCENARIO: " + str(scenario.name))
    # pytest.globalDict['scenario_name'] = scenario.name
    # pytest.globalDict['scenario_tags'] = scenario.tags
    # pytest.globalDict['feature_name'] = feature.name
    # pytest.globalDict['feature_tags'] = feature.tags
    # pytest.globalDict['feature_description'] = feature.description
    #
    # if "ui_web" in scenario.tags:
    #      hook_utils.before_scneario_browser_setup(scenario, pytest.globalDict)
    # if "ui_thick_client" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #      print("Thick client configuration")
    # if "mobile_web" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #      print("mobile_web configuration")
    # if "mobile_iOS" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #      print("mobile_iOS configuration")
    # if "mobile_android" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #      print("mobile_android configuration")


def pytest_bdd_after_scenario(scenario):
    print("this will be printed after scenario \n {}".format(scenario.name))
    # webdriver = driver.driver.get_driver()
    # webdriver.quit()

    # if "ui_web" in scenario.tags:
    #     hook_utils.after_scenario_browser_teardown(scenario, sys.argv, pytest.globalDict)
    # if "ui_thick_client" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #     print("Thick client configuration")
    # if "mobile_web" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #     print("mobile_web configuration")
    # if "mobile_iOS" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #     print("mobile_iOS configuration")
    # if "mobile_android" in scenario.tags and not hook_utils.is_parallel_execution(sys.argv):
    #     print("mobile_android configuration")


def pytest_sessionfinish(session, exitstatus):
    print("session finish")
