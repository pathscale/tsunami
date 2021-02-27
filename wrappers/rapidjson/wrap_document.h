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

    void set_int(const char* key, int value)
    {
        Value& s = d[key];
        s.SetInt(value);
    }

    void set_string(const char* key, const char* value)
    {
        Value& s = d[key];
        char buffer[20];
        int len = sprintf(buffer, value); // dynamically created string.
        s.SetString(buffer, len, d.GetAllocator());
        memset(buffer, 0, sizeof(buffer));
    }

//    NOT WORKING
//    void add_int(const char* key, int value)
//    {
//        Value s;
//        s.SetInt(value);
//        char buffer[20];
//        sprintf(buffer, key);
//        d.CopyFrom(s, d.GetAllocator());
//        memset(buffer, 0, sizeof(buffer));
//    }

    int get_int(const char* key)
    {
        Value& s = d[key];
        return s.GetInt();
    }

    const char* get_string(const char* key)
    {
        Value& s = d[key];
        return s.GetString();
    }

    const char* get_json()
    {
        StringBuffer buffer;
        Writer<StringBuffer> writer(buffer);
        d.Accept(writer);

        return buffer.GetString();
    }
};
#endif //TSUNAMI_TEST_H
