#include "Python.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int fac(int n)
{
    if (n < 2)
        return 1;

    return (n) * fac(n-1);
}

char *reverse(char *s)
{
    register char t, *p = s, *q = (s + (strlen(s) - 1));

    while (p < q)
    {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }

    return s;
}

int test()
{
    char s[BUFSIZ];

    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get %s\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get %s\n", reverse(s));
    return 0;
}

static PyObject * Extest_fac(PyObject *self, PyObject *args)
{
    // int res;
    // int num;
    // PyObject *retval;

    // res = PyArg_ParseTuple(args, "i", &num);
    // if (!res) {
    //     return NULL;
    // }
    // res = fac(num);
    // retval = (PyObject *)Py_BuildValue("i", res);
    // return retval;
    //
    int num;
    if (!PyArg_ParseTuple(args, "i", &num))
        return NULL;
    return (PyObject *)Py_BuildValue("i", fac(num));
}

static PyObject *Extest_doppel(PyObject *self, PyObject *args)
{
    char *orig_str;
    if (!PyArg_ParseTuple(args, "s", &orig_str))
        return NULL;
    return (PyObject *)Py_BuildValue("ss", orig_str, reverse(strdup(orig_str)));
}

static PyObject *Extest_test(PyObject *self, PyObject *args)
{
    test();
    return (PyObject *)Py_BuildValue("");
}

static PyMethodDef ExtestMethods[] = {
    {"fac", Extest_fac, METH_VARARGS},
    {"doppel", Extest_doppel, METH_VARARGS},
    {"test", Extest_test, METH_VARARGS},
    {NULL, NULL},
};

void initExtest()
{
    Py_InitModule("Extest", ExtestMethods);
}

