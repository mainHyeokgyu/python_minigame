import pygame
import time
import random
pygame.init() #pygame모듈의 함수를 사용하기 위해 초기화
screen=pygame.display.set_mode((800,400)) #게임 창 (너비,높이)
pygame.display.set_caption("Game") #게임 창 이름
running=1 #while문을 돌리기 위한 매개변수
clock=pygame.time.Clock()

#1단계 이미지파일
background=pygame.image.load("무궁화/background1.jpg")#1단계 배경
hurdle=pygame.image.load("무궁화/hurdle1-removebg-preview.png")
rock= pygame.image.load("무궁화/rock-removebg-preview.png")
r_light=pygame.image.load("무궁화/redlight.png")
g_light=pygame.image.load("무궁화/greenlight.png")
success=pygame.image.load("success-removebg-preview (1).png")
fail=pygame.image.load("fail-removebg-preview.png")

#2단계 이미지 파일
background_2=pygame.image.load("줄다리기/background2.png")#2단계 배경
rope=pygame.image.load("줄다리기/rope_normal.png")#줄다리기 하고있는 사진
ropeL=pygame.image.load("줄다리기/left_pull.png")
ropeR=pygame.image.load("줄다리기/right_pull.png")

direction=[    pygame.image.load("줄다리기/position/up.png"),
               pygame.image.load("줄다리기/position/down.png"),
               pygame.image.load("줄다리기/position/right.png"),
               pygame.image.load("줄다리기/position/left.png")] #방향키 사진
#3단계 이미지 파일
background_3 = pygame.image.load("홀짝/hol/holbackground.PNG")
board = pygame.image.load("홀짝/hol/board.jpg")
pocket = pygame.image.load("홀짝/hol/pocket.PNG")
pocket_text = pygame.image.load("홀짝/hol/pocket_text.PNG")
pocket_1 = pygame.image.load("홀짝/hol/pocket_1.PNG")
pocket_2 = pygame.image.load("홀짝/hol/pocket_2.PNG")
pocket_3 = pygame.image.load("홀짝/hol/pocket_3.PNG")
pocket_4 = pygame.image.load("홀짝/hol/pocket_4.PNG")
pocket_5 = pygame.image.load("홀짝/hol/pocket_5.PNG")
pocket_6 = pygame.image.load("홀짝/hol/pocket_6.PNG")
pocket_7 = pygame.image.load("홀짝/hol/pocket_7.PNG")
pocket_8 = pygame.image.load("홀짝/hol/pocket_8.PNG")
pocket_9 = pygame.image.load("홀짝/hol/pocket_9.PNG")
pocket_10 = pygame.image.load("홀짝/hol/pocket_10.PNG")
odd = pygame.image.load("홀짝/hol/button_odd.PNG")
even = pygame.image.load("홀짝/hol/button_even.PNG")
click_odd = pygame.image.load("홀짝/hol/click_odd.PNG")
click_even = pygame.image.load("홀짝/hol/click_even.PNG")
end_img = pygame.image.load("홀짝/hol/end.jpg")
#3단계
end = None

#print(pygame.font.get_fonts()) # 폰트 종류
Font_s = pygame.font.SysFont('gulim', 30)
Font_b = pygame.font.SysFont('gulim', 100)
black = (0, 0, 0)
white = (255, 255, 255)

life= 0 # 구슬 획득 현황
bead_goal = random.randint(20,25) # 구슬 획득 최종 목표

#사운드 설정
mugunghwa_L=[ pygame.mixer.Sound("무궁화/sounds/Squid Game Sound Effect x0.8.wav"),
            pygame.mixer.Sound("무궁화/sounds/Squid Game Sound Effect x1.6.wav"),
            pygame.mixer.Sound("무궁화/sounds/Squid Game Sound Effect x2.4.wav")]
#캐릭터 스프라이트 이미지 불러오기
MoveLeft=[pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__000.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__001.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__002.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__003.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__004.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__005.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__006.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__007.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__008.png'),0,0.1),
          pygame.transform.rotozoom(pygame.image.load('templerun/Left/LRun__009.png'),0,0.1)]

MoveRight=[pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__000.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__001.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__002.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__003.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__004.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__005.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__006.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__007.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__008.png'),0,0.1),
           pygame.transform.rotozoom(pygame.image.load('templerun/Right/Run__009.png'),0,0.1)]

#스프라이트 설정
left=False
right=False
stop=False
up=False
down=False
movecount=-1
lastmotion="LEFT" #마지막 이동 왼쪽=0,오른쪽=1
def ch_Move(left,right,up,down,stop):
    global movecount
    if movecount==-1:
        screen.blit(ch, (ch_x,ch_y)) #캐릭터 초기 위치
    if movecount>60:
        movecount=0
    if left:
        screen.blit(MoveLeft[movecount//10],(ch_x,ch_y))
        movecount+=1
    elif right:
        screen.blit(MoveRight[movecount//10],(ch_x,ch_y))
        movecount+=1
    elif stop:
        if lastmotion=="LEFT":                      #마지막 움직임이 왼쪽이었을 경우
            screen.blit(MoveLeft[0],(ch_x,ch_y))
        elif lastmotion=="RIGHT":                   #마지막 움직임이 오른쪽이었을 경우
            screen.blit(MoveRight[0],(ch_x,ch_y))
    elif up:
        if lastmotion=="LEFT":
            screen.blit(MoveLeft[movecount//10],(ch_x,ch_y))
        elif lastmotion=="RIGHT":
            screen.blit(MoveRight[movecount//10],(ch_x,ch_y))
        movecount+=1
    elif down:
        if lastmotion=="LEFT":
            screen.blit(MoveLeft[movecount//10],(ch_x,ch_y))
        elif lastmotion=="RIGHT":
            screen.blit(MoveRight[movecount//10],(ch_x,ch_y))
        movecount+=1
#장애물에 부딪혔을 때, 자연스러운 움직임
def smoothmove(hurdle_x,hurdle_y,hurdle_w,hurdle_h):
    global ch_x
    global ch_y
    if ch_x > hurdle_x+hurdle_w-1:
        ch_x+=2
        ch_x_vector = 0
    elif ch_x+ch_w < hurdle_x+1:
        ch_x-=2
        ch_x_vector = 0
    if ch_y > hurdle_y+hurdle_h -1:
        ch_y+=2
        ch_y_vector = 0
    elif ch_y+ch_h < hurdle_y+1:
        ch_y-=2
        ch_y_vector = 0

#캐릭터 화면 밖으로 벗어나지 않게 조정
def limitch():
    global ch_x
    global ch_y
    if ch_x>(800-ch_w):
        ch_x = (800-ch_w)
    elif ch_x<0:
        ch_x = 0
    if ch_y>(400-ch_h):
        ch_y = (400-ch_h)
    elif ch_y<0:
        ch_y = 0


#1단계 실패
success_1=0 #1단계 성공여부
def stage_1_miss():
    global running
    global success_1
    global s_time_1
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
             running=0
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                success_1=-1
            elif event.key == pygame.K_RIGHT:
                success_1=-1
            elif event.key == pygame.K_UP:
                success_1=-1
            elif event. key== pygame.K_DOWN:
                success_1=-1
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT:
                success_1=-1
            elif event.key== pygame.K_UP or event.key== pygame.K_DOWN:
                success_1=-1
    if(success_1==-1):
        s_time_1=time.time()        #실패시점
        success_1=-2
    
    
#캐릭터 크기,위치 설정
ch=MoveLeft[0]
ch_size=ch.get_rect().size
ch_w=ch_size[0]
ch_h=ch_size[1]
ch_x=(800-ch_w)
ch_y=400/2
ch_speed=0.5

ch_x_vector=0
ch_y_vector=0

#장애물
hurdle_size=hurdle.get_rect().size
hurdle_w=hurdle_size[0]
hurdle_h=hurdle_size[1]
hurdle_x=600
hurdle_y=400/2

hurdle2_x=450
hurdle2_y=100

hurdle3_x=300
hurdle3_y=320

hurdle4_x=100
hurdle4_y=0

rock_size=rock.get_rect().size
rock_w=rock_size[0]
rock_h=rock_size[1]
rock_x=120
rock_y=100

rock2_x=450
rock2_y=280

#신호등
r_light_size=r_light.get_rect().size
g_light_size=g_light.get_rect().size
r_light_x=-5
r_light_y=0
g_light_x=-5
g_light_y=0

#방향키 좌표설정(2단계)
direction_size=direction[0].get_rect().size
direction_w=direction_size[0]
direction_h=direction_size[1]
direction_x=(800/2-direction_w/2)
direction_y=50
#밧줄 좌표설정(2단계)
rope_size=rope.get_rect().size
rope_w=rope_size[0]
rope_h=rope_size[1]
rope_x=400-(rope_w/2)
rope_y=220
rope_speed=1

rope_x_vector=0

#3단계
# 보드, 주머니, 홀짝 버튼 _ 크기, 위치
board_size = board.get_rect().size
board_w = board_size[0]
board_h = board_size[1]
board_x = 800/2 - board_w/2
board_y = 0

pocket_size = pocket.get_rect().size
pocket_w = pocket_size[0]
pocket_h = pocket_size[1]
pocket_x = 800/2 - pocket_w - 50
pocket_y = 400/2 - pocket_h/2 +50

pocket_text_size = pocket_1_size = pocket_2_size = pocket_3_size = pocket_4_size = pocket_size
pocket_6_size = pocket_7_size = pocket_8_size = pocket_9_size = pocket_10_size = pocket_size


odd_size = odd.get_rect().size
odd_w = odd_size[0]
odd_h = odd_size[1]
odd_x = 800/2 + odd_w/2
odd_y = 400/2 - odd_h +40

click_odd_size = click_odd.get_rect().size
click_odd_w = click_odd_size[0]
click_odd_h = click_odd_size[1]
click_odd_x = odd_x
click_odd_y = odd_y

even_size = even.get_rect().size
even_w = even_size[0]
even_h = even_size[1]
even_x = 800/2 + even_w/2
even_y = 400/2 +60

click_even_size = click_even.get_rect().size
click_even_w = click_even_size[0]
click_even_h = click_even_size[1]
click_even_x = even_x
click_even_y = even_y

end_img_size = end_img.get_rect().size

# 버튼 위 마우스 유무
class Button:
    def __init__(self, img, x, y, w, h, what, click_img, x_click, y_click):
        state = ""
        mouse = pygame.mouse.get_pos()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            screen.blit(click_img, (x_click, y_click))

# 게임 종료 count
def count(endd, time):
    text_end = Font_s.render(str(time), True, white)
    screen.blit(text_end, [400, 50])
    return

# 3단계 main
mouse_button = 1
mouse_but = 1
game_hol = 1
oddeven = 1
term_3 = 3     # 설명 텀
sta=0
success_3=0
end_t=1


#성공 이모티콘
success_size=success.get_rect().size
success_w=success_size[0]
success_h=success_size[1]
success_x=800/2-success_w/2
success_y=400/2-success_h/2
#실패 이모티콘
fail_size=fail.get_rect().size
fail_w=fail_size[0]
fail_h=fail_size[1]
fail_x=800/2-fail_w/2
fail_y=400/2-fail_h/2

stage=1 #단계 설정
s_time_1=0 #1단계 성공시점 초기화
term=5.7 #초록불 지속시간 초기값
term_L=[5.7, 2.7, 1.5] #음성파일 배속에 따른 초록불 지속시간
init_time=time.time()+random.randint(1,3) #첫 초록불 시간
sound_num=0
beadtime_1=time.time()    #1단계 시작시간

keyboardN=0 #1은 위 2는 아래 3은 오른쪽 4는 왼쪽(2단계 키보드 입력값 초기화
direct=random.randint(1,4)   #방향키 초기값
rope_time=0 #컴퓨터가 밧줄 당기는 시간
success_2=0
beadtime_2=0    #2단계 구슬획득 기준 시간

while(running):
    e_time=time.time()             #현재시간
    dt=clock.tick(60)              #프레임 60fps 설정
    if stage==1:
        timer_1=Font_s.render("소요 시간: %d초" %int(e_time-beadtime_1) ,True,black)
        screen.blit(background, (0,0)) #배경(0,0)좌표부터 오른쪽아래로 채워줌
        if(e_time>init_time+term):
            sound_num=random.randint(0,2)
            init_time=e_time+term                                     #초록불 켜지는시간 업데이트
        if(e_time>init_time and e_time<init_time+term and success_1==0):             #초록불이 켜질 조건
            screen.blit(g_light, (g_light_x,g_light_y))                             #초록색신호등 띄우기
            screen.blit(timer_1, (320,0))   
            mugunghwa=mugunghwa_L[sound_num]                                      #음성 배속파일
            term=term_L[sound_num]                                              #소요시간
            mugunghwa.play()                                                  #사운드 재생
            for event in pygame.event.get():                                        #Key event
                if event.type== pygame.QUIT:
                    running=0
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ch_x_vector -= ch_speed  #ch_x_vector=ch_x_vector-ch_speed
                        left=True
                        stop=False
                        lastmotion="LEFT"
                    elif event.key == pygame.K_RIGHT:
                        ch_x_vector += ch_speed
                        right=True
                        stop=False
                        lastmotion="RIGHT"
                    elif event.key == pygame.K_UP:
                        ch_y_vector -= ch_speed
                        stop=False
                        up=True
                        down=False
                    elif event. key== pygame.K_DOWN:
                        ch_y_vector += ch_speed
                        stop=False
                        up=False
                        down=True
                if event.type == pygame.KEYUP:
                    if event.key== pygame.K_LEFT:
                        ch_x_vector = 0
                        stop=True
                        left=False
                        right=False
                        
                    if event.key== pygame.K_RIGHT:
                        ch_x_vector = 0
                        stop=True
                        right=False
                        left=False
                    elif event.key== pygame.K_UP or event.key== pygame.K_DOWN:
                        ch_y_vector = 0
                        stop=True
                        up=False
                        down=False
            #x축 이동
            ch_x += ch_x_vector*dt
            #y축 이동
            ch_y+=ch_y_vector*dt
            #hurdle과의 충돌
            if ch_x+ch_w > hurdle_x  and ch_x < (hurdle_x+hurdle_w):      #ch와 enemy의 부피 고려
                if ch_y+ch_h > (hurdle_y)  and ch_y < hurdle_y+hurdle_h:
                    smoothmove(hurdle_x,hurdle_y,hurdle_w,hurdle_h)
            if ch_x+ch_w > hurdle2_x  and ch_x < (hurdle2_x+hurdle_w):      #ch와 enemy의 부피 고려
                if ch_y+ch_h > (hurdle2_y)  and ch_y < hurdle2_y+hurdle_h:
                    smoothmove(hurdle2_x,hurdle2_y,hurdle_w,hurdle_h)
            if ch_x+ch_w > hurdle3_x  and ch_x < (hurdle3_x+hurdle_w):      #ch와 enemy의 부피 고려
                if ch_y+ch_h > (hurdle3_y)  and ch_y < hurdle3_y+hurdle_h:
                    smoothmove(hurdle3_x,hurdle3_y,hurdle_w,hurdle_h)
            if ch_x+ch_w > hurdle4_x  and ch_x < (hurdle4_x+hurdle_w):      #ch와 enemy의 부피 고려
                if ch_y+ch_h > (hurdle4_y)  and ch_y < hurdle4_y+hurdle_h:
                    smoothmove(hurdle4_x,hurdle4_y,hurdle_w,hurdle_h)
            if ch_x+ch_w > rock_x  and ch_x < (rock_x+rock_w):      #ch와 enemy의 부피 고려
                if ch_y+ch_h > (rock_y)  and ch_y < rock_y+rock_h:
                    smoothmove(rock_x,rock_y,rock_w,rock_h)
            if ch_x+ch_w > rock2_x  and ch_x < (rock2_x+rock_w):      #ch와 enemy의 부피 고려
                if ch_y+ch_h > (rock2_y)  and ch_y < rock2_y+rock_h:
                    smoothmove(rock2_x,rock2_y,rock_w,rock_h)
            
            limitch()
        elif (e_time>init_time and e_time<init_time+term)!=1 and success_1!=1:                                                                  #움직이면 안될 때
             screen.blit(r_light, (r_light_x,r_light_y))
             screen.blit(timer_1, (320,0))                                  #소요시간 띄우기
             stage_1_miss()                                                 #움직이면 안될 때, 움직인 경우
        if(success_1==-2):
            if(e_time-s_time_1<3):    #실패 3초 뒤에 게임 종료
                screen.blit(fail,(fail_x,fail_y))
            else:
                running=0
       
        if ch_x<70:                                              #결승선을 통과했을 때
            if success_1==0:    
                success_1=1
                s_time_1=time.time()
            if(e_time-s_time_1<3):                              #성공화면 3초 표시
                screen.blit(success,(success_x,success_y))
            else:
                stage=2
                if(e_time-beadtime_1<35):                        #클리어 시간에 따른 목숨 차등 지급
                    life=8
                elif(e_time-beadtime_1<40):
                    life=6
                elif(e_time-beadtime_1<45):
                    life=4
                elif(e_time-beadtime_1<50):
                    life=2
                else:
                    life=0
                beadtime_2=time.time()                          #2단계 시작시간 저장
        ch_Move(left,right,up,down,stop)                                    #캐릭터 스프라이트
        screen.blit(hurdle, (hurdle_x,hurdle_y))                         #장애물 그리기
        screen.blit(hurdle, (hurdle2_x,hurdle2_y)) 
        screen.blit(hurdle, (hurdle3_x,hurdle3_y)) 
        screen.blit(hurdle, (hurdle4_x,hurdle4_y))
        screen.blit(rock, (rock_x,rock_y))
        screen.blit(rock, (rock2_x,rock2_y))
        
    elif stage==2:
        screen.blit(background_2,(0,0))
        if success_2==0:
            timer_2=Font_s.render("소요 시간: %d초" %int(e_time-beadtime_2) ,True,black)
            screen.blit(timer_2,(320,0))
            if(keyboardN==0): #중복 입력 방지
                for event in pygame.event.get():    #키이벤트
                    if event.type==pygame.QUIT:
                        running=0
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_UP:  #키이벤트 위 1
                            keyboardN=1
                            
                        if event.key==pygame.K_DOWN:  #키이벤트 아래 2
                            keyboardN=2
                            
                        if event.key==pygame.K_RIGHT:  #키이벤트 오 3
                            keyboardN=3
                            
                        if event.key==pygame.K_LEFT:  #키이벤트 왼 4
                            keyboardN=4
                              
                    if event.type==pygame.KEYUP:
                        if event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:        
                            rope_x_vector=0
                            keyboardN=0
            if(keyboardN==direct): #올바른 방향키를 입력할경우
                rope_x_vector+=1
                rope=ropeR
                direct=random.randint(1,4)
                keyboardN=0
            else:
                if keyboardN==0:        #입력하고 있지 않을 경우
                    rope_x_vector=0
                else:                   #잘못 입력할 경우
                    rope_x_vector-=0.5
                    rope=ropeL
                    direct=random.randint(1,4)
                    keyboardN=0
                    
            screen.blit(direction[direct-1],(direction_x,direction_y))
            if(e_time-rope_time>0.7):                 #2초마다 컴퓨터가 당김
                rope_time=e_time
                rope_x_vector-=1
                rope=ropeL
            if(rope_x>500):                                                         #결승선을 통과했을 때
                success_2=1
            elif(rope_x<300-rope_w):
                success_2=-1
        elif success_2==1 or success_2==2:
            if success_2==1:
                success_2=2    
                s_time_1=time.time()
            if success_2==2:
                if(e_time-s_time_1<3):
                    screen.blit(success,(success_x,success_y))
                else:
                    if(e_time-beadtime_2<19):                        #클리어 시간에 따른 목숨 차등 지급
                        life+=8
                    elif(e_time-beadtime_2<21):
                        life+=6
                    elif(e_time-beadtime_2<23):
                        life+=4
                    elif(e_time-beadtime_2<25):
                        life+=2
                    elif(e_time-beadtime_2<27):
                        life+=1
                    else:
                        life+=0
                    stage=3
                    init_time_hol = time.time()
        elif success_2==-1 or success_2==-2:
            if success_2==-1:
                success_2=-2
                s_time_1=time.time()
            elif success_2==-2:
                if(e_time-s_time_1<3):
                    screen.blit(fail,(fail_x,fail_y))
                else:
                    running=0
                    pygame.quit()

        rope_x+=rope_x_vector*dt
        screen.blit(rope, (rope_x,rope_y)) #캐릭터 위치"""
    elif stage==3:
        screen.blit(background_3, (0, 0)) # 홀짝 게임 배경 시작
        if sta==0:
            init_time_hol = time.time()
            sta+=1
    
        if time.time() - init_time_hol < 1 + term_3*4: # 홀짝 게임 설명 및 설정
            if time.time() - init_time_hol > 1:
                text_0 = Font_s.render("앞의 게임에서 모은 구슬의 수 = 목숨 : %d개" %life, True, black)
                screen.blit(text_0, [100, 100])
            if time.time() - init_time_hol > 1 + term_3*1:
                text_1 = Font_s.render("홀짝 예측 실패 시 목숨 차감", True, black)
                screen.blit(text_1, [100, 150])
            if time.time() - init_time_hol > 1 + term_3*2:
                text_2 = Font_s.render("목표 이상의 구슬 획득 시 WIN", True, black)
                screen.blit(text_2, [100, 200])
            if time.time() - init_time_hol > 1 + term_3*3:
                text_3 = Font_s.render("목숨이 모두 소진 시 lOSE", True, black)
                screen.blit(text_3, [100, 250])
                
                
                
        
        
        else:                            
            ## 게임 진행
            
            if oddeven == 1:                           # 1. 홀수? 짝수? 랜덤 지정
                pocket_state = 0
                board_state = 0
                bead_num = random.randint(3, 8)         
                
                if bead_num % 2 == 1.:     # 홀수? 짝수? 정답
                    answer = "홀수"
                else:
                    answer = "짝수"
                    print(answer)
            
                print("// 참고 : %d, %s" %(bead_num, answer))
                oddeven = 2
                
                
            elif oddeven == 2:                          # 2. 답 입력 가능(대기)
                mouse = pygame.mouse.get_pos()    
                event = pygame.event.poll()
                choice = ""
                mouse_button = 0
    
     
                    
                if odd_x + odd_w > mouse[0] > odd_x and odd_y + odd_h > mouse[1] > odd_y:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:   # 버튼 클릭 인식
                        pocket_state = None
                        choice = "홀수"
                        oddeven = 3
                    
                if even_x + even_w > mouse[0] > even_x and even_y + even_h > mouse[1] > even_y:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pocket_state = None
                        choice = "짝수"
                        oddeven = 3
    
                    
                    
                    
                if event.type == pygame.QUIT:
                    running=0
    
            
            
            elif oddeven == 3:                          # 3. 채점
                pygame.time.delay(1000)
                pocket_state = bead_num
                print(pocket_state)
                if answer == choice:
                    print("정답 !!!!")
                    board_state = 1
                    life += bead_num
                    oddeven = 4                
                else:
                    print("오답 !!!!")
                    board_state = 2
                    life -= bead_num
                    oddeven = 4
     
                    
            elif oddeven == 4:                          # 4. 게임 end 여부 확인
                pygame.time.delay(3000)
                if life >= bead_goal:
                    end = " W  I  N "
                elif life <= 0:
                    end = " L O S E "
                else:
                    oddeven = 1
    
                
    
            ## 게임 화면       
            if end == None:
                screen.blit(board, (board_x, board_y))     # board
                if board_state == 0:
                    text_board = Font_s.render("    목표 : %d            획득 : %d   " %(bead_goal, life), True, white)
                elif board_state == 1:
                    text_board = Font_s.render("구슬 : %d개 - %s     ! ! 정답 ! !" %(bead_num, answer), True, black)
                else:
                    text_board = Font_s.render("구슬 : %d개 - %s     ! ! 오답 ! !" %(bead_num, answer), True, black)
                screen.blit(text_board, [200, board_h/2 - 20])
            
                if pocket_state == None:                   # pocket
                    screen.blit(pocket, (pocket_x, pocket_y))  # pocket_홀?짝? 정답?오답?
                elif pocket_state == 0:
                    screen.blit(pocket_text, (pocket_x, pocket_y)) # pocket_text
                elif pocket_state == 1:
                    screen.blit(pocket_1, (pocket_x, pocket_y))
                elif pocket_state == 2:
                    screen.blit(pocket_2, (pocket_x, pocket_y))
                elif pocket_state == 3:
                    screen.blit(pocket_3, (pocket_x, pocket_y))
                elif pocket_state == 4:
                    screen.blit(pocket_4, (pocket_x, pocket_y))
                elif pocket_state == 5:
                    screen.blit(pocket_5, (pocket_x, pocket_y))
                elif pocket_state == 6:
                    screen.blit(pocket_6, (pocket_x, pocket_y))
                elif pocket_state == 7:
                    screen.blit(pocket_7, (pocket_x, pocket_y))
                elif pocket_state == 8:
                    screen.blit(pocket_8, (pocket_x, pocket_y))
                elif pocket_state == 9:
                    screen.blit(pocket_9, (pocket_x, pocket_y))
                elif pocket_state == 10:
                    screen.blit(pocket_10, (pocket_x, pocket_y))

            
                
                screen.blit(odd, (odd_x, odd_y))           # odd_num_마우스 유무
                oddbutton = Button(odd, odd_x, odd_y, odd_w, odd_h, 1, click_odd, click_odd_x, click_odd_y)    
            
                screen.blit(even, (even_x, even_y))        # even_num_마우스 유무
                evenbutton = Button(even, even_x, even_y, even_w, even_h, 2, click_even, click_even_x, click_even_y)
            
            
            else:
                oddeven=5
                screen.blit(end_img, (0, 0))
                text_result = Font_b.render(end, True, white)
                screen.blit(text_result, [215, 150])   
                        
                        
                if end_t == 1:
                    end_time = time.time()
                    end_t = 0
            
    
                if time.time() - end_time > 2:
                    if time.time() - end_time  < 4:
                        text_end = Font_s.render("잠시 후 게임이 종료됩니다.", True, white)
                        screen.blit(text_end, [240, 70])
            
                    elif time.time() - end_time < 6:
                        count(end, 6)
                    elif time.time() - end_time < 8:
                        count(end, 4)
                    elif time.time() - end_time < 10:
                        count(end, 2)
                    else:
                        running = 0
    pygame.display.update()                                             #게임화면 업데이트
    
pygame.quit()
#캐릭터스프라이트,장애물,골인지점,장애물,enemy,배경 다 바꾸기, 음성파일 배속파일 만들기
