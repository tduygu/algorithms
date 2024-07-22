"""This code lists :
 * the instagram followers of your account
 * the people who you follow - followings
 * followers that you don't follow
 * not followers that you follow

 You must change the files under insta_files directory
 with your followers and followings files which must be in instagram's json file format
"""
import json

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
        print(f)
    return lst_follower

def get_names_following(stream_var):
    z = json.loads(stream_var)
    # z['relationships_following'][0]['string_list_data'][0]['value']
    lst_following = []
    for s in z['relationships_following']:
        f = s['string_list_data'][0]['value']
        lst_following.append(f)
        print(f)
    return lst_following

print("Followers",end='\n')
follower_var = get_json_content('../insta_files/followers_1.json')
follower_lst = get_names_followers(follower_var)
print(f"Number of follower= {len(follower_lst)}")

print("Followings",end='\n')
following_var = get_json_content('../insta_files/following.json')
following_lst = get_names_following(following_var)
print(f"Number of followings = {len(following_lst)}")

not_followers = []
for ff in following_lst:
    if ff not in follower_lst:
        not_followers.append(ff)

print("NOT FOLLOWERS THAT I FOLLOW")
print(f"Takipçi olmayan takip edilen sayısı: {len(not_followers)}")
for nf in not_followers:
    print(nf)


print("FOLLOWERS THAT I DON'T FOLLOW")
not_following=[]
for ff in follower_lst:
    if ff not in following_lst:
        not_following.append(ff)

print(f"Takip etmediğim takipçiler: {len(not_following)}")
for nf in not_following:
    print(nf)


