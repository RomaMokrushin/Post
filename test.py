global_servers = dict()
print('Вас приветствует помощник!')
print("Чтобы начать пользоваться почтой напишите mail.MailClient('Любое название сервера', 'Любое имя пользователя')")


class MailClient:
    global global_servers

    def __init__(self, server, user):
        who_are_you = user
        self.who_are_you = user
        new_server = dict()
        new_server[who_are_you] = []
        global_servers[server] = new_server
        print('Вас рада приветствовать почта')
        print('Для дополнительной информации напишите info()')

    def send_mail(self, server, user, message):
        if server not in global_servers:
            print(f'FAIL: {server} not found')
        elif user in global_servers[server]:
            global_servers[server][user].append(message)
        else:
            print(f'FAIL: {user} not found')

    def add_server(self, server):
        global_servers[server] = dict()

    def add_user(self, server, user):
        global_servers[server][user] = []

    def receive_mail(self, server, user, how):
        if server in global_servers and user in global_servers[server]:
            if how == 'all':
                clone = global_servers[server][user]
                del global_servers[server][user]
                return clone
            elif how == 'last':
                clone = global_servers[server][user][-1]
                del global_servers[server][user][-1]
                return clone
            elif ('0' in str(how) or '1' in str(how) or '2' in str(how) or '3' in str(how) or '4' in str(
                    how) or '5' in str(how) or '6' in str(how) or '7' in str(how) or '8' in str(how) or '9' in str(
                    how)) and '.' not in str(how) and ',' not in str(how):
                if how > len(global_servers[server][user]) + 1:
                    clone = global_servers[server][user]
                    del global_servers[server][user]
                    return clone
                clone = global_servers[server][user][:how]
                del global_servers[server][user]
                return clone
            return f"Invalid Name of 'how'"
        return f'Invalid Name of Server or User'

    def postbox(self):
        counter = 0
        for i in global_servers:
            if self.who_are_you in global_servers[i]:
                for _ in global_servers[i][self.who_are_you]:
                    counter = counter + 1
        return f'{counter} не прочитанных писем'

    def change_account(self, user):
        self.who_are_you = user
        return f'{self.who_are_you} - имя нового профиля'

    def profile(self):
        return f'{self.who_are_you} - имя вашего профиля'

    def when(self, user):
        answer = list()
        for i in global_servers:
            if user in global_servers[i]:
                answer.append(i)
        return answer

    def check(self):
        answer = list()
        clone = global_servers
        for i in global_servers:
            if self.who_are_you in clone[i]:
                for j in clone[i][self.who_are_you]:
                    answer.append(j)
                    global_servers[i][self.who_are_you].clear()
        return answer

    def info(self):
        print('-----------')
        print("Метод: 'send_mail(server, user, message)' принимает название сервера"
              " и имя пользователя на которое вы хотите отправить 'message', а также вы заходите в аккаунт"
              " под именем этого пользователя")
        print("Метод: 'add_server(server)' принимает название сервера который вы хотите создать")
        print("Метод: 'add_user(server, user)' принимает название сервера на который вы хотите добавить пользователя"
              " и его имя")
        print("Метод: 'receive_mail(server, user, how)' принимает значение сервера и имя пользователя с которого вы"
              " хотите считать письма, а также принимает команду 'how' указав значение которой: 'all' она вернет все"
              " письма, а если вы хотите не все напишите число: количество писем начиная от самых старых какие хотите"
              " прочитать. Или же 'last' если захотите прочитать последее")
        print("Метод: 'when(user)', принимает имя пользователя и возвращает все названия серверов отправка сообщения"
              " данному пользователю возможна")
        print("Метод: 'all()' выводит на экран все сервера со всеми пользователями и их письмами")
        print("Метод: 'postbox()' возвращает ваше не прочитанное количество писем")
        print("Метод: 'profile()' возвращает ваше текущее имя пользователя")
        print("Метод: 'check()' возвращает все ваши не прочитанные письма")
        print("Метод: 'info()' вам сейчас помогает :)")
        print('-----------')

    def all(self):
        print(global_servers)