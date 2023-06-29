"""
test_drag_drop.py
Drag and Drop: Exercise locator.drag_to() and page.mouse methods

[Scenario]
Drag box a and drop at the position of box b
Drag box a and drop at the position of box b, again
Drag box b and drop at the position of box a
Drag box b and drop at the position of box a, again

[Young's comment]


"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_drag_drop_by_playwright(BasePage):
    page :Page = BasePage

    # go to 'Drag and Drop' page
    pageName = 'Drag and Drop'
    page.get_by_role('link', name=pageName).click()
    expect(page.get_by_role('heading')).to_have_text(pageName)

    # check if both box a and b are draggable
    expect(page.locator("div[draggable='true']").first).to_have_text('A')
    expect(page.locator("div[draggable='true']").last).to_have_text('B')

    boxA = page.locator("div[draggable='true']").filter(has_text='A')
    boxB = page.locator("div[draggable='true']").filter(has_text='B')

    # drag box a and drop at the position of box b
    boxA.drag_to(boxB)
    expect(page.locator("div[draggable='true']").first).to_have_text('B')

    # drag box a and drop at the position of box b, again
    boxA.drag_to(boxB)
    expect(page.locator("div[draggable='true']").first).to_have_text('A')

    # drag box b and drop at the position of box a
    boxB.drag_to(boxA)
    expect(page.locator("div[draggable='true']").first).to_have_text('B')

    # drag box b and drop at the position of box a, again
    boxB.drag_to(boxA)
    expect(page.locator("div[draggable='true']").first).to_have_text('A')
    
    # test again with mouse methods
    posLeft = page.locator("div[draggable='true']").first.bounding_box()
    assert posLeft != None
    posLeft['center_x'] = posLeft['x'] + posLeft['width'] / 2
    posLeft['center_y'] = posLeft['y'] + posLeft['height'] / 2
    posRight = page.locator("div[draggable='true']").last.bounding_box()
    assert posRight != None
    posRight['center_x'] = posRight['x'] + posRight['width'] / 2
    posRight['center_y'] = posRight['y'] + posRight['height'] / 2

    # drag box a and drop at the position of box b
    page.mouse.move(posLeft['center_x'], posLeft['center_y'])
    page.mouse.down()
    page.mouse.move(posRight['center_x'], posRight['center_y'])
    page.mouse.up()
    expect(page.locator("div[draggable='true']").first).to_have_text('B')

    # drag box a and drop at the position of box b, again
    page.mouse.move(posRight['center_x'], posRight['center_y'])
    page.mouse.down()
    page.mouse.move(posLeft['center_x'], posLeft['center_y'])
    page.mouse.up()
    expect(page.locator("div[draggable='true']").first).to_have_text('A')

    # drag box b and drop at the position of box a
    page.mouse.move(posRight['center_x'], posRight['center_y'])
    page.mouse.down()
    page.mouse.move(posLeft['center_x'], posLeft['center_y'])
    page.mouse.up()
    expect(page.locator("div[draggable='true']").first).to_have_text('B')

    # drag box b and drop at the position of box a, again
    page.mouse.move(posLeft['center_x'], posLeft['center_y'])
    page.mouse.down()
    page.mouse.move(posRight['center_x'], posRight['center_y'])
    page.mouse.up()
    expect(page.locator("div[draggable='true']").first).to_have_text('A')



    