## NPM

# package.json {#package}

~~~~~~~~~~js
{
  ...
  "dependencies": {
    ...
    "rapidjson_wrapper": "git@github.com:Tencent/rapidjson_wrapper.git"
  },
  ...
  "gypfile": true
}
~~~~~~~~~~

# binding.gyp {#binding}

~~~~~~~~~~js
{
  ...
  'targets': [
    {
      ...
      'include_dirs': [
        '<!(node -e \'require("rapidjson_wrapper")\')'
      ]
    }
  ]
}
~~~~~~~~~~
