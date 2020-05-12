from selenium import webdriver
import time
browser = webdriver.Chrome()

url = 'https://r.xiumi.us/board/v5/4CaFX/212468289'

def start():
    browser.get(url)
    time.sleep(1)
    btn = browser.find_element_by_css_selector('body > div.tn-reader-paper.container.ng-scope > section.row.tn-article-body > article.tn-cube-box.paper.dock-loader.atom-data-binding.ng-scope.tn-comp-anim-pin.tn-comp-inst.tn-cube-box-inst.tn-comp.tn-in-cell-state-active.tn-from-house-reader_booklet-cp > section > div.tn-cube-slot.tn-view-cubes.ng-scope.tn-cell-inst.tn-cell.tn-cell-group.tn-child-position-absolute.tn-state-active.tn-cube-flipper-box > div > section > div.dock.booklet.tn-page-slot.tn-view-pages.ng-scope.tn-cell-inst.tn-cell.tn-cell-group.tn-child-position-absolute.tn-state-active.tn-vertical-flipper-box > div > section > div > div > section > div > div:nth-child(16) > section > div:nth-child(2) > div > div.tn-comp-anim-pin.tn-comp.tn-from-house-paper-cp.ng-scope.tn__dark-item__220 > section > div > div.tn__dark-item__225 > div.tn__dark-item__226 > label > input')
    btn.click()
    sub = browser.find_element_by_css_selector('body > div.tn-reader-paper.container.ng-scope > section.row.tn-article-body > article.tn-cube-box.paper.dock-loader.atom-data-binding.ng-scope.tn-comp-anim-pin.tn-comp-inst.tn-cube-box-inst.tn-comp.tn-in-cell-state-active.tn-from-house-reader_booklet-cp > section > div.tn-cube-slot.tn-view-cubes.ng-scope.tn-cell-inst.tn-cell.tn-cell-group.tn-child-position-absolute.tn-state-active.tn-cube-flipper-box > div > section > div.dock.booklet.tn-page-slot.tn-view-pages.ng-scope.tn-cell-inst.tn-cell.tn-cell-group.tn-child-position-absolute.tn-state-active.tn-vertical-flipper-box > div > section > div > div > section > div > div:nth-child(16) > section > div:nth-child(2) > div > div.tn-comp-anim-pin.tn-comp.tn-from-house-paper-cp.ng-scope.tn__dark-item__221 > a > section > div > p > strong')
    sub.click()
    return None

def main():
    start()

if __name__ == '__main__':
    for i in range(200):
        main()