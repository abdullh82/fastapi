from operator import mod
from sys import prefix
from .. import models,schemas
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional,List
from .. import outh2

router=APIRouter(prefix="/posts",tags=['Posts'])

#selece * from posts
#@router.get("/",response_model=List[schemas.Post])
@router.get("/",response_model=List[schemas.Postout])

async def get_posts(db : Session=Depends(get_db),current_user:int=Depends(outh2.get_current_user),limit:int=10,skip:int=0,searsh:Optional[str]=""):
    print(limit)
    # posts=db.query(models.Post).filter(models.Post.title.contains(searsh)).limit(limit).offset(skip).all()
    result=db.query(models.Post,func.count(models.Votes.post_id).label("vote")).join(models.Votes,models.Votes.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(searsh)).limit(limit).offset(skip).all()
   
    return  result


#create post
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
async def create_post(post:schemas.PostCreate,db : Session=Depends(get_db),current_user:int=Depends(outh2.get_current_user)):
    # cursor.execute("""insert into posts (title,content,published) values (%s,%s,%s) 
    # returning *""",(post.title,post.content,post.published))
    # new_post=cursor.fetchone()
    # conn.commit()
    #new_post=models.Post(title=post.title,content=post.content,published=post.published)
    new_post=models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@router.get("/{id}",response_model=schemas.Postout)
async def get_post(id:int,response:Response,db : Session=Depends(get_db),current_user:int=Depends(outh2.get_current_user)):
    # cursor.execute(F"select * from posts where id ={id}")
    # post=cursor.fetchone()
    # post=db.query(models.Post).filter(models.Post.id==id).first()
    post=db.query(models.Post,func.count(models.Votes.post_id).label("vote")).join(models.Votes,models.Votes.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
   
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id}")
    
    
    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int,db : Session=Depends(get_db),current_user:int=Depends(outh2.get_current_user)):
    # cursor.execute(""" delete from posts where id = %s returning * """,(str(id),))
    # deleted_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if  post==None:
       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with not exist id : {id}")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.Post)
async def update_post(id:int,post:schemas.PostCreate,db : Session=Depends(get_db),current_user:int=Depends(outh2.get_current_user)):
    # cursor.execute("""update posts set title=%s ,content=%s,published=%s where id  = %s returning * """,(post.title,post.content,post.published,str(id)))
    # update_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    print(type(current_user))
    post_t=post_query.first()
    if  post_t==None:
       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with not exist id : {id}")
    # post_query.update({'title':'oneoneone','content':'dlkdldldjlk'},synchronize_session=False)
    if post_t.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")

    
    post_query.update(post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()



