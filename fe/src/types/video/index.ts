export type IVideo = {id:string,name:string,url:string,formats:IFormat[]}

type IFormat = {
    type:"720p" | "360p" |'480p' |"240p" |"144p" | "audio";
    url:string;
}