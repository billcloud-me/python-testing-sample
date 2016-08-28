# Python Testing Sample
[![Build Status](https://travis-ci.org/billcloud-me/python-testing-sample.svg?branch=master)](https://travis-ci.org/billcloud-me/python-testing-sample)

This python package is my attempt to test out python testing methods.  Currently the module has unit testing with pytest tests and BDD testing with Behave.  The package is linked to TravisCI for automatic testing when changes are pushed via git.

## Unit Testing

The unit tests are located in the [tests](https://github.com/billcloud-me/python-testing-sample/tree/master/tests) directory and are written in [pytest](http://doc.pytest.org/en/latest/).

## BDD Testing

Behavior Driven Development features are located in the [features](https://github.com/billcloud-me/python-testing-sample/tree/master/features) directory and the steps for these feaatures are in the [features/steps](https://github.com/billcloud-me/python-testing-sample/tree/master/features/steps) directory.  The features are writtin in [Gherkin](https://github.com/cucumber/cucumber/wiki/Gherkin) and are part of [Behave](http://pythonhosted.org/behave/).

## TravisCI

The test results are located on TravisCI for this [repo](https://travis-ci.org/billcloud-me/python-testing-sample).
