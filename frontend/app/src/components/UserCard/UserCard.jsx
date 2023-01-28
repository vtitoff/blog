import React from 'react'
import classes from './UserCard.module.css'

const UserCard = (props) => {
    return (
        <div className={classes.wrapper}>
            <div className={classes.container}>
                {props.data}
            </div>
        </div>
    )
}

export default UserCard;