import React from 'react'
import classes from './Header.module.css'
// import header__logo from "../../images/logo.png";

const Header = (props) => {
    return (
        <header className={classes.header}>
            <div className={classes.header_container}>
                <img className={classes.header__logo} src={'#'} alt="logo"/>
            </div>
        </header>
    )
}

export default Header;