#include <stdio.h>
#include <string.h>

void cprint(char *s)
{
    printf("%s", s);
}
char* btoc(bool val)
{
    if (val)
        return "True";
    else
        return "False";
}
char* itoc(int val)
{
    char str[20];
    sprintf(str, "%d", val);
    return str;
}
char* constCharToChar(const char* str)
{
    return strdup(str);
}