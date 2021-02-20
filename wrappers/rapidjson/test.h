//
// Created by NOIDEA on 2021-02-20.
//

#ifndef TSUNAMI_TEST_H
#define TSUNAMI_TEST_H

#include "../../core/third-party/rapidjson/include/rapidjson/document.h"
#include "../../core/third-party/rapidjson/include/rapidjson/writer.h"
#include "../../core/third-party/rapidjson/include/rapidjson/stringbuffer.h"
#include <iostream>

using namespace rapidjson;
class Doc
{
    private:
    Document d;

    public:
    Doc(const char* json)
    {
        d.Parse(json);
    }

    Doc()
    {
        //yes
    }

    void change(const char* value, int amount)
    {
        Value& s = d[value];
        s.SetInt(amount);
    }

    const char* get()
    {
        StringBuffer buffer;
        Writer<StringBuffer> writer(buffer);
        d.Accept(writer);

        return buffer.GetString();
    }
};
#endif //TSUNAMI_TEST_H
