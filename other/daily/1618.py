"""
1618. 找出适应屏幕的最大字号
给定一个字符串 text。并能够在 宽为 w 高为 h 的屏幕上显示该文本。

字体数组中包含按升序排列的可用字号，您可以从该数组中选择任何字体大小。

您可以使用FontInfo接口来获取任何可用字体大小的任何字符的宽度和高度。

FontInfo接口定义如下：

interface FontInfo {
  // 返回 fontSize 大小的字符 ch 在屏幕上的宽度。
  // 每调用该函数复杂度为 O(1)
  public int getWidth(int fontSize, char ch);

  // 返回 fontSize 大小的任意字符在屏幕上的高度。
  // 每调用该函数复杂度为 O(1)
  public int getHeight(int fontSize);
}
一串字符的文本宽度应该是每一个字符在对应字号(fontSize)下返回的宽度getHeight(fontSize)的总和。

请注意：文本最多只能排放一排

如果使用相同的参数调用 getHeight 或 getWidth ，则可以保证 FontInfo 将返回相同的值。

同时，对于任何字体大小的 fontSize 和任何字符 ch ：

getHeight(fontSize) <= getHeight(fontSize+1)
getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)
返回可用于在屏幕上显示文本的最大字体大小。如果文本不能以任何字体大小显示，则返回-1。

示例 1:

输入: text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]
输出: 6
Example 2:

输入: text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]
输出: 4
Example 3:

输入: text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]
输出: -1



"""


# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
class FontInfo(object):
   # Return the width of char ch when fontSize is used.
   def getWidth(self, fontSize, ch):
       """
       :type fontSize: int
       :type ch: char
       :rtype int
       """

   def getHeight(self, fontSize):
       """
       :type fontSize: int
       :rtype int
       """

class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        fonts_len = len(fonts)

        left = 0
        right = fonts_len - 1
        while left <= right:
            mid = (left + right) >> 1
            if self.cal_data(fontInfo, fonts[mid], text, w, h):
                left = mid + 1
            else:
                right = mid - 1
        if self.cal_data(fontInfo, fonts[right], text, w, h):
            return fonts[right]
        return -1

    def cal_data(self, api, fontsize, text, w, h):
        w_sum = 0
        if api.getHeight(fontsize) > h:
            return False
        for _ in text:
            w_sum += api.getWidth(fontsize, _)
        return w_sum <= w