#include <stdio.h>

void greet(){
    printf("Hello, World!\n");
    fflush(stdout);
}

#include "Python.h"

static PyObject *helloWorld_greet(PyObject *self, PyObject *args){
    greet();
    Py_RETURN_NONE;
}

static PyMethodDef helloWorldMethods[] =
{
    {"greet", helloWorld_greet, METH_VARARGS}
};

void inithelloWorld(){
    Py_InitModule("helloWorld", helloWorldMethods);
}