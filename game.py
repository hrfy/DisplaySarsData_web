#！coding=utf-8
# @Version : 1.0
# @Time    : 2020/1/20  
# @Author  : hua rong



print('■■■■■■■■■■ 欢迎来到地下城，送死的凡人 ■■■■■■■■■■')
print('''
     ,            _..._            ,
    {'.         .'     '.         .'}
    { ~ '.      _|=    __|_      .'  ~}
  { ~  ~ '-._ (___________) _.-'~  ~  }
 {~  ~  ~   ~.'           '. ~    ~    }
{  ~   ~  ~ /   /\     /\   \   ~    ~  }
{   ~   ~  /    __     __    \ ~   ~    }
 {   ~  /\/  -<( o)   ( o)>-  \/\ ~   ~}
  { ~   ;(      \/ .-. \/      );   ~ }
   { ~ ~\_  ()  ^ (   ) ^  ()  _/ ~  }
    '-._~ \   (`-._'-'_.-')   / ~_.-'
        '--\   `'._'+'_.'`   /--'
            \     \`-'/     /
             `\    '-'    /'
               `\       /'
                 '-...-' 
''')
print('''
           ,
          / \\
         {   }
         !   !
         ; : ;
         | : |
         | : |
         l ; l
         l ; l
         I ; I
         I ; I
         I ; I
         I ; I
         d | b 
         H | H
         H | H
         H I H
 ,;,     H I H     ,;,
;H@H;    ;_H_;,   ;H@H;
`\Y/d_,;|4H@HK|;,_b\Y/'
 '\;MMMMM$@@@$MMMMM;/'
   ~~~*; !8@8!; *~~~
         ;888;
         ;888;
         ;888;
         ;888;
         d8@8b
         O8@8O
         T808T
          `~` 
''')
print("In the following sequential numbers, replace all numbers containing 7 and multiples of 7 with X:")
for i in range(1,101):
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        print("X"),
    else:
        print(i),

