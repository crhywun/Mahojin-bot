import requests
import time
import sys

# ==========================================
# 配置部分
# ==========================================
MY_COOKIE = "_ga=GA1.1.275674206.1771219900; __Secure-next-auth.csrf-token=e0adb9c12b0c6e8cede3675d21fcd7731e9ddcf7dfb5ff4f8aa61d12bd449575%7Caf6cff13f4a2a9ecaf044d2be42ab762c84c9263d9582cae5dee1e6b9c52c9cf; __Secure-next-auth.callback-url=https%3A%2F%2Fapp.mahojin.ai%2F; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..zNTQPpQVf1p_XxPy.rTPauN3LRhMaHih0yuowT-Vy8xOIdhag-Bm68fAkMDWThL2Kme9HPN2NVgVlgWDCPsWYCToiR06QdTBtE273HShgo5bGG8kj-kuJarxHdFEMxtMynLpUM9kz4zmyb2NtTP5S7gcf3Og3rqPzroioJE_-f7LFwMg3oF34ynwYkelGpq-KX_x3Ymuc12nZ3FPqDG4YIMCAzhMxicFNFfYXKAuHvDM40Gb7xQ.s3b2Pqq7ByU6Grw6qG4jqw; _ga_VXKT1K1GXW=GS2.1.s1771229598$o4$g1$t1771229700$j45$l0$h0"

class MahojinCheckIn:
    def __init__(self, cookie):
        self.session = requests.Session()
        self.base_url = "https://app.mahojin.ai"
        self.headers = {
            "authority": "app.mahojin.ai",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ko;q=0.6",
            "content-type": "application/json",
            "cookie": cookie,
            "origin": "https://app.mahojin.ai",
            "referer": "https://app.mahojin.ai/maho-point",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

    def get_timezone_offset(self):
        return time.timezone // 60 if time.localtime().tm_isdst == 0 else time.altzone // 60

    def get_user_status(self):
        print("[*] 正在检查登录状态...")
        url = f"{self.base_url}/api/point"
        try:
            response = self.session.get(url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                print(f"[+] 登录成功！当前总积分: {data.get('point', 0)}")
                return True
            else:
                print(f"[-] 登录失败 (状态码: {response.status_code})")
                print(f"[-] 响应内容: {response.text}")
                return False
        except Exception as e:
            print(f"[-] 请求异常: {e}")
            return False

    def check_in(self):
        print("[*] 正在尝试签到...")
        url = f"{self.base_url}/api/user/check-in"
        payload = {"timezoneOffset": self.get_timezone_offset()}
        try:
            response = self.session.post(url, headers=self.headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                print(f"[+] 签到成功! 获得积分: {data.get('amount', '未知')}")
            else:
                try:
                    res_json = response.json()
                    print(f"[-] 签到失败: {res_json.get('message', '今天可能已经签到过了')}")
                except:
                    print(f"[-] 签到失败 (状态码: {response.status_code}): {response.text}")
        except Exception as e:
            print(f"[-] 签到过程出现异常: {e}")

if __name__ == "__main__":
    bot = MahojinCheckIn(MY_COOKIE)
    if bot.get_user_status():
        bot.check_in()
