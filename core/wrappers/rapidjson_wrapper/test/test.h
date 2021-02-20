//
// Created by kacpe on 2/20/2021.
//

#ifndef TSUNAMI_TEST_H
#define TSUNAMI_TEST_H

#include "../includes/rapidjson.h"
#include <stdio.h>
using namespace rapidjson;

class Doc{
    private:
        Document document;

    public:
        Doc(){}
        Doc(char* json){
            document = Document();
            document.Parse(json);
        }

        bool HasError()
        {
            return (this->document.HasParseError());
        }

        char* GetError()
        {
            char str[64];
            if (this->HasError())
                sprintf(str, "Error(offset %u): %s",
                    (unsigned)document.GetErrorOffset(),
                    GetParseError_En(document.GetParseError())
                );
            return str;
        }
};

int test(char* json) {
    ////////////////////////////////////////////////////////////////////////////
    // 1. Parse a JSON text string to a document.

    //const char json[] = " { \"hello\" : \"world\", \"t\" : true , \"f\" : false, \"n\": null, \"i\":123, \"pi\": 3.1416, \"a\":[1, 2, 3, 4] } ";
    //const char *jsonConst = &json[0];
    // printf("Original JSON:\n %s\n", json);

    Document document;  // Default template parameter uses UTF8 and MemoryPoolAllocator.

    // "normal" parsing, decode strings to new buffers. Can use other input stream via ParseStream().
    if (document.Parse(json).HasParseError())
    {
        fprintf(stderr, "\nError(offset %u): %s\n",
            (unsigned)document.GetErrorOffset(),
            GetParseError_En(document.GetParseError()));
        return (unsigned)document.GetErrorOffset();
    }
    return 0;
}

#endif //TSUNAMI_TEST_H
