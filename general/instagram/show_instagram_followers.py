"""This code lists :
 * the instagram followers of your account
 * the people who you follow - followings
 * followers that you don't follow
 * not followers that you follow

 You must change the files under insta_files directory
 with your followers and followings files which must be in instagram's json file format
"""
import json

ACCOUNTNAME= "kitapkahvemuhabbet"
FILEOUTNAME= '../insta_files/'+ACCOUNTNAME+'.txt'
SEPR = "\n"+'─' * 40+"\n"+ '-'*40+'\n'

def get_json_content(filename):
    try:
        stream = open(filename)
        stream_var = stream.read()
        return stream_var
    except Exception as e:
        print(f"Error: {e.errno} - {e}")
    finally:
        stream.close()

def get_names_followers(stream_var):
    y = json.loads(stream_var)
    # print(y[0]['string_list_data'][0]['value'])
    lst_follower = []
    for s in y:
        f = s['string_list_data'][0]['value']
        lst_follower.append(f)
        #print(f)
    return lst_follower

def get_names_following(stream_var):
    z = json.loads(stream_var)
    # z['relationships_following'][0]['string_list_data'][0]['value']
    lst_following = []
    for s in z['relationships_following']:
        f = s['string_list_data'][0]['value']
        lst_following.append(f)
        #print(f)
    return lst_following


def write_to_file(content, filename, add):
    try:
        file_mod = 'a' if add else 'w'
        stream = open(filename, file_mod)
        stream.write(content)

        stream.close()
    except Exception as e:
        print("An error occured.")


write_to_file(ACCOUNTNAME + SEPR, FILEOUTNAME, False)
print("Followers",end='\n')
follower_var = get_json_content('../insta_files/followers_1.json')
follower_lst = get_names_followers(follower_var)
print(f"Number of followers= {len(follower_lst)}")
write_to_file(f"Number of followers= {len(follower_lst)} \n", FILEOUTNAME, True)


print("Followings",end='\n')
following_var = get_json_content('../insta_files/following.json')
following_lst = get_names_following(following_var)
print(f"Number of followings = {len(following_lst)}")
write_to_file(f"Number of followings = {len(following_lst)} {SEPR}", FILEOUTNAME, True)

not_followers = []
follow_to_follow_list = []
for ff in following_lst:
    if ff not in follower_lst:
        not_followers.append(ff)
    elif ff in follower_lst:
        follow_to_follow_list.append(ff)

print("NOT FOLLOWERS THAT I FOLLOW")
write_to_file("NOT FOLLOWERS THAT I FOLLOW \n",FILEOUTNAME, True)
write_to_file(f"Takipçi olmayan takip edilen sayısı: {len(not_followers)} \n",FILEOUTNAME, True)
print(f"Takipçi olmayan takip edilen sayısı: {len(not_followers)}")
not_followers_str = '\n'.join(not_followers)
#print(not_followers_str)
write_to_file(not_followers_str + SEPR, FILEOUTNAME, True)

print("FOLLOW TO FOLLOW")
print((f"Karşılıklı takipte olduklarımız: {len(follow_to_follow_list)}"))
write_to_file((f"FOLLOW TO FOLLOW\n Karşılıklı takipte olduklarımız: {len(follow_to_follow_list)}\n"),FILEOUTNAME,True)
follow_to_follow_str = "\n".join(follow_to_follow_list)
write_to_file(follow_to_follow_str + SEPR,FILEOUTNAME,True)


not_following=[]
for ff in follower_lst:
    if ff not in following_lst:
        not_following.append(ff)
print("FOLLOWERS THAT I DON'T FOLLOW")
print(f"Takip etmediğim takipçiler: {len(not_following)}")
write_to_file(f"FOLLOWERS THAT I DON'T FOLLOW \n Takip etmediğim takipçiler: {len(not_following)} \n",FILEOUTNAME,True)
not_following_str = "\n".join(not_following)
write_to_file(not_following_str + SEPR,FILEOUTNAME,True)

