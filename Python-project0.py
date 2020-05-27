{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# تمارين لغة بايثون"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "مرحبًا، هذا الملف سيكون تقييمًا جيدًا لنا لمعرفة مهارتنا في لغة بايثون  \n",
    "من المهم لنا أن نتقن استخدام الأداة حتى نحقق أهدافنا، و أداتنا في هذا المعسكر هي لغة بايثون  \n",
    "سنطلب منك حل التحديات القصيرة أدناه، لتتمكن من تقييم نفسك ، بالتوفيق!\n",
    "\n",
    "ملاحظة: لا يوجد حل واحد صحيح، و هذا ما يميز البرمجة حقًا"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### المهمة الأولى"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "لدينا أربعة متغيرات هنا، هل يمكننا برمجيًا معرفة نوع هذه المتغيرات؟  \n",
    "يرجى كتابة الحل المقترح"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'bool'>\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "x = 7\n",
    "y = x/3\n",
    "z = x == 7\n",
    "s = \"Hello python programmer!\"\n",
    "print (type(x))\n",
    "print (type(y))\n",
    "print (type(z))\n",
    "print (type(s))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### المهمة الثانية"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "نرغب بطباعة الجملة التالية:  \n",
    "\"I want to pay 10.5 riyals for 2 pieces of this item.\"  \n",
    "لكننا سنقوم باستخدام المتغيرات المعرفة لدينا (متغير السعر ومتغير الكمية) بدلا من إعادة كتابة الأرقام، هل يمكنك فعلها؟"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I want to pay 10.5 riyals for 2 pieces of this item.\n"
     ]
    }
   ],
   "source": [
    "quantity = 2\n",
    "price = 10.5\n",
    "text = \"I want to pay \" +str(price) +\" riyals for \" +str(quantity) + \" pieces of this item.\" \n",
    "print(text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### المهمة الثالثة"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "قم بكتابة دالة تقوم بمقارنة الرقم المدخل (مثل ١٩) بالرقم ١٠ و تخبرك ما إذا كان أكبر من الرقم ١٠ أم لا"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19 is bigger than 10\n"
     ]
    }
   ],
   "source": [
    "def bigger_than_10(x):\n",
    "    if x>10:\n",
    "        print (str(x) + \" is bigger than 10\")\n",
    "    else:\n",
    "        print (str(x) + \" is not bigger than 10\")\n",
    "        \n",
    "bigger_than_10(19)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### المهمة الرابعة"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "لدينا قائمة من الفواكه، كيف يمكننا برمجيا الحصول على آخر فاكهتين في القائمة؟"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "melon\n",
      "mango\n"
     ]
    }
   ],
   "source": [
    "fruites = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\"]\n",
    "print(fruites[5])\n",
    "print(fruites[6])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "هل يمكننا طباعة كل عنصر من القائمة السابقة في سطر مستقل؟"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n",
      "orange\n",
      "kiwi\n",
      "melon\n",
      "mango\n"
     ]
    }
   ],
   "source": [
    "for f in fruites:\n",
    "    print (f)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### المهمة الخامسة"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "لنفترض أن لدينا المعجم التالي، نريد إضافة المفتاح  \n",
    "black  \n",
    "بالقيمة  \n",
    "000000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "colors = {\n",
    "  \"blue\": \"0000FF\",\n",
    "  \"green\": \"00FF00\",\n",
    "  \"yellow\": \"FFFF00\",\n",
    "  \"red\": \"FF0000\",\n",
    "  \"white\": \"unknown\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'blue': '0000FF', 'green': '00FF00', 'yellow': 'FFFF00', 'red': 'FF0000', 'white': 'unknown', 'black': '000000'}\n"
     ]
    }
   ],
   "source": [
    "colors['black']='000000'\n",
    "print(colors)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "هل يمكننا تغيير قيمة المفتاح  \n",
    "white  \n",
    "بالقيمة  \n",
    "FFFFFF ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'blue': '0000FF', 'green': '00FF00', 'yellow': 'FFFF00', 'red': 'FF0000', 'white': 'FFFFFF', 'black': '000000'}\n"
     ]
    }
   ],
   "source": [
    "colors['white']='FFFFFF'\n",
    "print(colors)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "نريد إنشاء دالة تقوم بأخذ قائمة و استبدال عناصرها بالقيم من المعجم بالاستعانة بالمفاتيح\n",
    "مثال: نستبدل  \n",
    "blue  \n",
    "  بالقيمة  \n",
    "  0000FF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "def exchange_values(lista):\n",
    "    #print (colors)\n",
    "    #print (lista)\n",
    "    \n",
    "   # print (\"new line\")\n",
    "    \n",
    "    k=list(colors.keys())\n",
    "    #print(k)\n",
    "    \n",
    "    v=list(colors.values())\n",
    "    #print(v)\n",
    "    \n",
    "    x=0\n",
    "    y=0\n",
    "    while x<6:\n",
    "        while y<6:\n",
    "            if lista[x]==k[y]:\n",
    "                lista[x]=v[y]\n",
    "            else:\n",
    "                y+=1\n",
    "        y=0\n",
    "        x+=1\n",
    "    print(lista) \n",
    "            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['0000FF', 'FFFFFF', '000000', 'FFFF00', '00FF00', 'FF0000']\n"
     ]
    }
   ],
   "source": [
    "lista = ['blue', 'white', 'black', 'yellow', 'green', 'red']\n",
    "exchange_values(lista)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
