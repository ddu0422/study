package jpabook.start

import javax.persistence.Column
import javax.persistence.Entity
import javax.persistence.Id
import javax.persistence.Table

@Entity
@Table(name="MEMBER")
class Member(
    @Id
    @Column(name = "id")
    private val id: String = "",

    @Column(name = "name")
    private val username: String = "",

    private val age: Int = 0
)
