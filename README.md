# Python Testing Sample

![](http://jenkins.billcloud.me:8080/buildStatus/icon?job=python-testing-sample)

[Build Status](http://jenkins.billcloud.me:8080/job/python-testing-sample/)

This python package is my attempt to test out python testing methods.  Currently the module has unit testing with pytest tests and BDD testing with Behave.  The package is linked to TravisCI for automatic testing when changes are pushed via git.

## Unit Testing

The unit tests are located in the [tests](https://github.com/billcloud-me/python-testing-sample/tree/master/tests) directory and are written in [pytest](http://doc.pytest.org/en/latest/).

## BDD Testing

Behavior Driven Development features are located in the [features](https://github.com/billcloud-me/python-testing-sample/tree/master/features) directory and the steps for these feaatures are in the [features/steps](https://github.com/billcloud-me/python-testing-sample/tree/master/features/steps) directory.  The features are writtin in [Gherkin](https://github.com/cucumber/cucumber/wiki/Gherkin) and are part of [Behave](http://pythonhosted.org/behave/).

## JenkinsCI

The test results are located on JenkinsCI for this [repo](http://jenkins.billcloud.me:8080/job/python-testing-sample/).
