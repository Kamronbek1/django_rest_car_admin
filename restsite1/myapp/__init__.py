#
# '''
# https://github.com/deschler/django-modeltranslation/issues/407
# '''
#
#
# class I18nModelSerializer(serializers.ModelSerializer):
#     def create_functions(names):
#         # Loop over the names
#         for name in names:
#             # Create a lambda function that returns the attribute of the object with the name "hello_" + the language code
#             func = lambda self, obj: getattr(obj, f"{name}_{self.context.get('request').LANGUAGE_CODE}", None)
#
#             # Set the function name to "get_" + name
#             func.__name__ = f"get_{name}"
#
#             # Set the function as an attribute of the current class
#             setattr(self.__class__, f"get_{name}", func)
#
#     # Create a list of function names
#     names = ["name", "color", ]
#
#     # Call the function to create dynamic functions
#     create_functions(names)
#
#     # def make_getter(name):
#     #     def get_name(self, obj):
#     #         lang = self.context.get("request").LANGUAGE_CODE
#     #         return getattr(obj, f"{name}_{lang}", None)
#     #
#     #     get_name.__name__ = f"get_{name}"
#     #     return get_name
#     #
#     # def gen_fun(self):
#     #     fields = getattr(self.Meta, 'i18n_fields', None)
#     #     lang = self.context.get("request").LANGUAGE_CODE
#     #     for name in fields:
#     #         sname = f'{name}_{lang}'
#     #         locals()[f"{name}"] = serializers.CharField(source=sname)
#     #         # self.make_getter(name)
#     #
#     # def generate_functions(function_list):
#     #     code = ""
#     #     for name in function_list:
#     #         code += "sname = f" + name + "_{self.context.get(\'request\').LANGUAGE_CODE}\"\n"
#     #         code += "locals()[" + name + "] = serializers.CharField(source=sname)\n"
#     #     exec(code)
#     #
#     # generate_functions(['color', 'name'])
#
#     # def get_name(self, obj):
#     #     fields = getattr(self.Meta, 'i18n_fields', None)
#     #     print(fields)
#     #     print(self.context.get("request").LANGUAGE_CODE)
#     #     # return 'name for tes asd dsa dasd sdt'
#     #     return [getattr(obj, f"{field}_{self.context.get('request').LANGUAGE_CODE}", None) for field in fields]
#
#     # def generate_fields(self, obj):
#     #     for field in super().Meta.i18n_fields:
#     #         locals()[f"get_{field}"] = lambda obj: getattr(obj, f"{field}_{self.context.get('request').LANGUAGE_CODE}", None)
#     # functions = []
#     #
#     # for field in super().Meta.i18n_fields:
#     #     print(field)
#     # def get_field_names(self, declared_fields, info):
#     #     fields = super().get_field_names(declared_fields, info)
#     #     print(fields)
#
#
# class TranslationModelSerializer(serializers.ModelSerializer):
#     pass
#     # def get_field_names(self, declared_fields, info):
#     #     fields = super().get_field_names(declared_fields, info)
#     #     lang = (
#     #         self.context.get("request").LANGUAGE_CODE
#     #         if self.context.get("request")
#     #         else None
#     #     )
#     #     if lang:
#     #         i18n_fields = getattr(self.Meta, 'i18n_fields', None)
#     #         print('fields ', i18n_fields)
#     #         result = []
#     #         for f in fields:
#     #             result.append(f)
#     #         for k in i18n_fields:
#     #             result.append("{}_{}".format(k, lang))
#     #             # result.append(getattr(info, f"{k}"))
#     #     else:
#     #         result = fields
#     #     return result
#     # hello = serializers.SerializerMethodField()
#
#     # def get_hello1(self, obj):
#     #     lang = self.context.get("request").LANGUAGE_CODE
#     #     return getattr(obj, f"name_{lang}", None)
#     #
#     # hel = get_hello1()
#     # hello = serializers.CharField(source=f"name_{self.context.get('request').LANGUAGE_CODE}")
#
#
# class LangSerializer(serializers.ModelSerializer):
#     # a metaclass that adds multi language fields and methods to the serializer class
#     class MetaLang(type):
#         def __new__(cls, name, bases, attrs):
#             # get the multi language fields from the Meta class
#             lang_fields = attrs['Meta'].lang_fields
#             # loop through the multi language fields
#             for field in lang_fields:
#                 # add a field with the same name
#                 attrs[field] = serializers.SerializerMethodField()
#
#                 # add a method with the same name prefixed with get_
#                 def get_field(self, obj):
#                     # get the user language from the request
#                     user_lang = self.context['request'].LANGUAGE_CODE
#                     # get the field attribute based on the user language
#                     field_attr = f'{field}_{user_lang}'
#                     # return the field value if it exists, otherwise None
#                     return getattr(obj, field_attr, None)
#
#                 attrs[f'get_{field}'] = get_field
#             # create the serializer class
#             print(type.__new__(cls, name, bases, attrs))
#             return type.__new__(cls, name, bases, attrs)
#
#     # use the metaclass for the serializer class
#     __metaclass__ = MetaLang
#
#     # class Meta:
#     #     # define the multi language fields in a tuple
#     #     # lang_fields = ()
#     #     pass
#
#
# # class CarSerializer(TranslationModelSerializer):
