import React from 'react'
import { NavLink } from 'react-router-dom'
import { Menu } from 'semantic-ui-react'

export default function NavMenu() {
    return(
        <Menu as='nav' size='massive' stackable inverted>
            <Menu.Item>
                <NavLink exact to='/'>Home</NavLink>
            </Menu.Item>
            <Menu.Item>
                <NavLink to='/drivers'>Drivers</NavLink>
            </Menu.Item>
            <Menu.Item>
                <NavLink to='/tracks'>Tracks</NavLink>
            </Menu.Item>
            <Menu.Item>
                <NavLink to='/schedule'>Schedule</NavLink>
            </Menu.Item>
        </Menu>
    )
}