#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <unistd.h>


/* Acquire the GIL and sleep for seconds given in args[0] */
static PyObject *
gil_acquire_gil(PyObject *self, PyObject *args)
{
    unsigned int sleep_seconds;
    PyGILState_STATE gstate;

    if (!PyArg_ParseTuple(args, "I", &sleep_seconds)) {
        return NULL;  // PyArg_ParseTuple has raised an exception.
    }

    gstate = PyGILState_Ensure();

    if (!PyGILState_Check()) {
        PyErr_SetString(PyExc_RuntimeError, "Couldn’t acquire the GIL");
        return NULL;
    }

    sleep(sleep_seconds);

    PyGILState_Release(gstate);
    Py_RETURN_NONE;
}

static PyMethodDef GilMethods[] = {
    {
        "acquire_gil",
        gil_acquire_gil,
        METH_VARARGS,
        "Acquire the GIL and sleep for given seconds"
    },
    {NULL, NULL, 0, NULL}  /* Sentinel */
};

static struct PyModuleDef gilmodule = {
    PyModuleDef_HEAD_INIT,
    "gil",    /* name of module */
    NULL,     /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    GilMethods
};

PyMODINIT_FUNC
PyInit_gil(void)
{
    return PyModule_Create(&gilmodule);
}
