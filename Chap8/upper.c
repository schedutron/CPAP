#include <math.h>
#include <stdio.h>
#include <ctype.h>

char *uppercase(char *string){
    char *s = string;
    while(*s){
        *s = toupper((unsigned char) *s);
        s++;
    }
    return string;
}

int main(){
    char string[5] = "hEllo";
    printf("%s\n", uppercase(string));
    return 0;
}

#include "Python.h"

static PyObject *upper_uppercase(PyObject *self, PyObject *args){
    char *orig_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "s", &orig_str))
        return NULL;
    retval = (PyObject*)Py_BuildValue("s", uppercase(orig_str));
    return retval;
}

static PyMethodDef upperMethods[] =
{
    {"to_uppercase", upper_uppercase, METH_VARARGS}
};

void initupper(){
    Py_InitModule("upper", upperMethods);
}